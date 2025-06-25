from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from src.app.controllers.api import demo_controller
from src.app.controllers.pages import page_controller

app = FastAPI()

app.mount("/static", StaticFiles(directory="src/resources/static"), name="static")

app.include_router(page_controller.router)
app.include_router(demo_controller.router)
