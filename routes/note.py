from fastapi import APIRouter,status
from models.note import Note
from config.db import client
from schema.note import noteEntity,notesEntity
from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
note=APIRouter()## router name
templates = Jinja2Templates(directory="templates")
@note.get("/", response_class=HTMLResponse)

async def read_item(request: Request):
    note= client.notes.doc.find({})
    
    newnote=[]
    for n in note:
        newnote.append({
            "_id":n["_id"],
             "author":n["author"],
            "text":n["text"],
            
        })
    return templates.TemplateResponse(
        request=request, name="index.html",context={"newnote":newnote}
    )
# @note.post("/")
# def addNote(note:Note):
#     inserted_note=client.notes.docs.insert_one(dict(note))
#     return noteEntity(inserted_note)
## use python-multipart module for post request

@note.post("/")
async def create_item(request:Request):
    form=await request.form()
    dictform=dict(form)
    
    note=client.notes.doc.insert_one(dict(form))
    
    return {"Success":True}
    
