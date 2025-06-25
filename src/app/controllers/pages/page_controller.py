from fastapi import APIRouter
from fastapi.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory="src/resources/templates")

router = APIRouter(
    prefix="",
    tags=["Pages"],
    default_response_class=HTMLResponse
)

# Startseite
@router.get("/",  name="home")
def home(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
    })