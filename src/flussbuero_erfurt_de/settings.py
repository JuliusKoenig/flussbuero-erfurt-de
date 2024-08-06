from typing import Literal

from wiederverwendbar.pydantic.singleton import ModelSingleton
from wiederverwendbar.logger import LoggerSettings


class Settings(LoggerSettings, metaclass=ModelSingleton):
    # log
    log_level: LoggerSettings.LogLevels = LoggerSettings.LogLevels.DEBUG

    # server
    server_host: str = "0.0.0.0"
    server_port: int = 80

    # website
    website_title: str = "Flussbüro Erfurt"
    website_slogan: str = "Ihr Partner für fließende Gewässer"
    website_responsible_for_content: str = "Dipl.-Ing. (FH) Stephan Gunkel"
    website_author: str = "Julius König"
    website_keywords: list[str] = [  # ToDo: Abstimmen mit Stephan, Einbinden in Website
        "Brücke",
        "Donau",
        "Elbe",
        "Erfurt",
        "FFH",
        "Fauna-Flora-Habitat-Richtlinie",
        "Fischotter",
        "Fließgewässer",
        "Fluss",
        "Flussbilder",
        "Flussbüro",
        "Gewässer",
        "Gewässerentwicklung",
        "Gewässerschutz",
        "Gewässerunterhaltung",
        "Hochwasser",
        "Hochwasserschutz",
        "Hochwasserschutz",
        "Ilm",
        "Ingenieurbiologie",
        "Ingenieurbüro",
        "Limnologie",
        "Luftbild",
        "Managementplan",
        "Managementplan",
        "Naturnaher Hochwasserschutz",
        "Oder",
        "Planung",
        "Renaturierung",
        "Retention",
        "Rhein",
        "Saale",
        "Strukturgütekartierung",
        "UVP",
        "Ulster",
        "Umweltverträglichkeitsprüfung",
        "Umweltverträglichkeitsprüfung",
        "Unstrut",
        "Versalzung",
        "WRRL",
        "Wasserbau",
        "Wasserbau",
        "Wasserrahmenrichtlinie",
        "Wasserrecht",
        "Wasserwirtschaft",
        "Wasserwirtschaft",
        "Werra",
        "Weser",
        "bautechnische Gesamtplanung",
    ]
    website_default_theme_mode: Literal["light", "dark"] = "light"
    website_charset: str = "utf-8"
    website_language: str = "de"
    website_viewport: str = "width=device-width, initial-scale=1, shrink-to-fit=no"
    website_theme_color: str = "#11679a"
    website_home_page: str = "/home"
    website_template_path: str = "templates"
    website_statics_path: str = "statics"
    website_statics_web_path: str = "/statics"
    website_statics_js_folder: str = "js"
    website_statics_css_folder: str = "css"
    website_statics_img_folder: str = "img"
    website_js: list[str] = ["vendor/jquery-3.7.1.min.js",
                             "vendor/tabler.min.js"]
    website_css: list[str] = ["vendor/tabler.min.css",
                              "style.css"]

    @property
    def website_statics_js_web_path(self) -> str:
        return f"{self.website_statics_web_path}/{self.website_statics_js_folder}"

    @property
    def website_statics_css_web_path(self) -> str:
        return f"{self.website_statics_web_path}/{self.website_statics_css_folder}"

    @property
    def website_statics_img_web_path(self) -> str:
        return f"{self.website_statics_web_path}/{self.website_statics_img_folder}"

    @property
    def website_js_web_paths(self) -> list[str]:
        return [f"{self.website_statics_js_web_path}/{js}" for js in self.website_js]

    @property
    def website_css_web_paths(self) -> list[str]:
        return [f"{self.website_statics_css_web_path}/{css}" for css in self.website_css]

    def get_img_web_path(self, img: str) -> str:
        return f"{self.website_statics_img_web_path}/{img}"
