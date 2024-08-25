from pydantic import BaseModel
class Note(BaseModel):
    author:str
    text:str
   
