from pathlib import Path

from starlette.applications import Starlette
from starlette.routing import Route
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

from flussbuero_erfurt_de.settings import Settings

WORK_DIR = Path(__file__).parent

settings: Settings = Settings()


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

    def setup_app(self):
        self.app = Starlette(
            debug=self.debug,
            routes=self.routes
        )

    def setup_routes(self):
        self.routes.append(Route("/", endpoint=self.home, methods=["GET"]))

    def setup_templates(self):
        self.templates = Jinja2Templates(directory=WORK_DIR / Settings().website_template_path)

    def setup_statics(self):
        self.app.mount(Settings().website_statics_web_path, StaticFiles(directory=WORK_DIR / Settings().website_statics_path), name="statics")

    async def _template_response(self, page_template_name: str, request: Request, context: dict):
        return self.templates.TemplateResponse(f"pages/{page_template_name}.html.jinja2", {"request": request, "settings": settings, **context})

    async def home(self, request: Request):
        return await self._template_response("home", request, {})


server = Server()
