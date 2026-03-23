from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes.note import note
from routes import about

app = FastAPI()
app.include_router(note)
app.include_router(about.router)

app.mount("/static", StaticFiles(directory="static"), name="static")
