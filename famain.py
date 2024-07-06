# import fastapi
from fastapi import FastAPI
from router import blog_get
from router import blog_post
from router import user
from db import models
from db.database import engine
from crud import crudmodels
# create an instance of the FastAPI class
app = FastAPI()
app.include_router(user.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)
# localhost:8000
# /docs shows automatically generated documentation

# the way to start a server with uvicorn is to provide the name of the file and the name of the instance
# uvicorn [filename]:[instance of server name] ie file main instance app
# get is the operation
@app.get('/') 
# creates a get method that invokes the index function, placing it on the '/' path
# if I were to go to localhost:8000, it would return 'hello world'
# if I change the path to '/hello', it would return 'hello world' if I go to localhost:8000/hello
def index():
    return 'hello world'

@app.post('/hello')
def index2():
    # curly brackets return a json (J.ava S.cript O.bject N.otation) object
    # collection of key value pairs similar to a dictionary
    # JSON is language-agnostic and can be used for data interchange between different programming languages

    return {'message': 'hi'}

# STEP 2: this runs the database
# whatever that means
crudmodels.Base.metadata.create_all(engine)
models.Base.metadata.create_all(engine)