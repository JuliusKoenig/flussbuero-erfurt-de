import uvicorn

from flussbuero_erfurt_de.settings import Settings

if __name__ == "__main__":
    uvicorn.run("flussbuero_erfurt_de:server", host=Settings().server_host, port=Settings().server_port, reload_dirs=["."], reload=True, factory=True)
