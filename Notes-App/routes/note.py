from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter
from models.note import Note
from config.db import conn
from schema.note import noteEntity, notesEntity
from fastapi.responses import RedirectResponse
from bson import ObjectId

note = APIRouter()

templates = Jinja2Templates(directory="templates")

@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    try:
        if not conn:
            return templates.TemplateResponse("index.html", {"request": request, "newDocs": [], "error": "Database connection failed"})
        
        docs = conn.notes.notes.find({})
        newDocs = []
        for doc in docs:
            newDocs.append({
                "id" : str(doc["_id"]),
                "title" : doc["title"],
                "desc" : doc["desc"],
                "important" : doc["important"],
            })
        return templates.TemplateResponse("index.html", {"request":request, "newDocs":newDocs})
    except Exception as e:
        return templates.TemplateResponse("index.html", {"request": request, "newDocs": [], "error": str(e)})


@note.post("/")
async def add_items(request: Request):
    try:
        if not conn:
            return RedirectResponse("/", status_code=303)
        form = await request.form()
        formDict = dict(form)
        noteData = {
            "title": formDict.get("title"),
            "desc": formDict.get("desc"),
            "important": True if formDict.get("important") == "on" else False
        }
        note = conn.notes.notes.insert_one(noteData)
        return RedirectResponse("/", status_code=303)
    except Exception as e:
        print(f"Error adding note: {e}")
        return RedirectResponse("/", status_code=303)


@note.get("/delete/{id}")
async def delete_note(id: str):
    try:
        if not conn:
            return RedirectResponse("/", status_code=303)
        conn.notes.notes.delete_one({"_id": ObjectId(id)})
        return RedirectResponse("/", status_code=303)
    except Exception as e:
        print(f"Error deleting note: {e}")
        return RedirectResponse("/", status_code=303)


@note.get("/edit/{id}", response_class=HTMLResponse)
async def edit_note(request: Request, id: str):
    try:
        if not conn:
            return templates.TemplateResponse("edit.html", {"request": request, "error": "Database connection failed"})
        doc = conn.notes.notes.find_one({"_id": ObjectId(id)})

        return templates.TemplateResponse(
            "edit.html",
            {
                "request": request,
                "note": doc,
                "id": id
            })
    except Exception as e:
        print(f"Error fetching note: {e}")
        return templates.TemplateResponse("edit.html", {"request": request, "error": str(e)})

@note.post("/update/{id}")
async def update_note(request: Request, id: str):
    try:
        if not conn:
            return RedirectResponse("/", status_code=303)
        form = await request.form()
        formDict = dict(form)

        updateData = {
            "title": formDict.get("title"),
            "desc": formDict.get("desc"),
            "important": formDict.get("important") == "on"
        }

        conn.notes.notes.update_one(
            {"_id": ObjectId(id)},
            {"$set": updateData}
        )
        return RedirectResponse("/", status_code=303)
    except Exception as e:
        print(f"Error updating note: {e}")
        return RedirectResponse("/", status_code=303)
    return RedirectResponse("/", status_code=303)
