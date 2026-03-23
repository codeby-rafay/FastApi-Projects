# routes/about.py
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    # Render the About Us page
    return templates.TemplateResponse("about.html", {"request": request})
