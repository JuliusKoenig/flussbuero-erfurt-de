from wiederverwendbar.logger import LoggerSingleton
from flussbuero_erfurt_de.settings import Settings

LoggerSingleton(name="flussbuero-erfurt-de",
                settings=Settings(init=True),
                ignored_loggers_like=[],
                ignored_loggers_equal=[], init=True)

from flussbuero_erfurt_de.server import server
