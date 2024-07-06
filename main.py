from fastapi import FastAPI
from db import models
from db.database import engine

app = FastAPI()

@app.get('/') # creates a get method that invokes the index function, placing it on the home path
def index():
    return 'hello world'

