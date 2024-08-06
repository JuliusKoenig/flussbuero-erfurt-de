from pathlib import Path
from typing import Literal, TypeVar

from starlette.applications import Starlette
from starlette.routing import Route
from starlette.requests import Request
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from starlette.exceptions import HTTPException

from flussbuero_erfurt_de.settings import Settings

WORK_DIR = Path(__file__).parent

settings: Settings = Settings()

ModuleTypes = TypeVar("ModuleTypes", Literal["page", "error"], Literal["page", "error"])


class Server:
    def __init__(self):
        self.debug: bool = True
        self.app: Starlette | None = None
        self.routes: list[Route] = []
        self.templates: Jinja2Templates | None = None

        # setup
        self.setup_routes()
        self.setup_templates()
        self.setup_app()
        self.setup_statics()

    def __call__(self, *args, **kwargs) -> Starlette:
        return self.app

    def setup_routes(self):
        self.routes.append(Route("/", endpoint=self.root, methods=["GET"], name="root"))
        self.routes.append(Route(settings.website_home_page, endpoint=self.home, methods=["GET"], name="home"))

    def setup_templates(self):
        self.templates = Jinja2Templates(directory=WORK_DIR / Settings().website_template_path)

    def setup_app(self):
        self.app = Starlette(
            debug=self.debug,
            routes=self.routes,
            exception_handlers={404: self.not_found, 500: self.server_error}  # type: ignore
        )

    def setup_statics(self):
        self.app.mount(Settings().website_statics_web_path, StaticFiles(directory=WORK_DIR / Settings().website_statics_path), name="statics")

    async def _template_response(self, template_name: str, request: Request, module: ModuleTypes = "page", **kwargs) -> Jinja2Templates.TemplateResponse:
        # get theme mode query param
        theme_mode = request.query_params.get("theme", None)

        # get theme mode cookie
        if theme_mode is None:
            theme_mode = request.cookies.get("theme_mode", settings.website_default_theme_mode)

        # get sure theme mode is valid
        theme_mode = "dark" if theme_mode == "dark" else "light"

        response = self.templates.TemplateResponse(f"modules/{module}s/{template_name}.html.jinja2", {"request": request,
                                                                                                      "settings": settings,
                                                                                                      "server": server,
                                                                                                      "theme_mode": theme_mode,
                                                                                                      **kwargs})
        # set theme mode cookie
        response.set_cookie("theme_mode", theme_mode)

        return response

    @classmethod
    async def root(cls, request: Request) -> RedirectResponse:
        return RedirectResponse(url=request.url_for("home"))

    async def not_found(self, request: Request, exc: HTTPException) -> Jinja2Templates.TemplateResponse:
        return await self._template_response("404", request, "error")

    async def server_error(self, request: Request, exc: HTTPException) -> Jinja2Templates.TemplateResponse:
        return await self._template_response("500", request, "error")

    async def home(self, request: Request) -> Jinja2Templates.TemplateResponse:
        return await self._template_response("home", request)


server = Server()
