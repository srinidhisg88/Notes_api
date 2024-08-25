# from typing import Union

from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
url='mongodb://127.0.0.1:27017/'
client=MongoClient(url)

app = FastAPI()




