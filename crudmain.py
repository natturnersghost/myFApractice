from typing import List
from pydantic import BaseModel
from fastapi import FastAPI, Depends, Request
from crud.MLS import mlsSchemas
from crud.MLS.mlsSchemas import UserDisplay 
from datetime import datetime
from sqlalchemy.orm import Session
from mlsDB.mlsdatabase import get_db
from crud import crudmodels
from mlsDB.mlsdatabase import engine
from crud.crudmodels import bills
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app1 = FastAPI()
app2 = FastAPI()
job_counter = 0
#CRUD 
#HTTP methods: GET, POST, PUT, DELETE
# this is Retrive
# getting something from the server
@app1.get('/todos', tags=['GET part of crud'])
def get_all_todos():
    return todos

@app1.get('/todos/{todo_id}', tags=['GET part of crud'])
def get_todo(
    todo_id: str,
):
    """ Get all todos """
    return todos.get(todo_id)
# has to return a dictionary
# if you path in the key I will give you the value

# create a dictionary to return
todos = {
    # 'id_1' is a key with the value of another dictionary
    "id_1": {
        "title": "Todo 1",
        "description": "Todo 1 description"
    },
    "id_2": {
        "title": "Todo 2",
        "description": "Todo 2 description"
    },
    "id_3": {
        "title": "Todo 3",
        "description": "Todo 3 description"
    }
}
class Todo(BaseModel):
    title: str
    description: str

@app1.delete("/todo/{todo_id}", tags=["DELETE part of CRUD"])
def delete_todo(
    todo_id: str,
):
    todos.pop(todo_id)
    return "todo deleted"
    #remove todo with given id
    #pop is a python method that removes something from a dictionary

###

###
@app1.post('/todo/post', tags=["POST part of CRUD"])
def create_todo(
    data: Todo
):
    todo_id = f'id_{len(todos)+1}' 
    # creates a new todo_id that is the number of total posts + 1
     # 'todos' -> 'todo_id' 
    todos[todo_id] = {

        'title': data.title,
        'description': data.description
    }   
    #return the post you just created
    return todos[todo_id]

# pass id, title and description
@app1.put("/todo/{todo_id}")
def update_todo(
    todo_id: str,
    data: Todo
):
    #update todo with given id
    todos[todo_id] = {
        "title" : data.title,
        "description": data.description
    }

    return todos[todo_id]

# //////////////////////////////////////////////////////////////// #
# //////////////////////////////////////////////////////////////// #
# //////////////////////////////////////////////////////////////// #
#@app1.post ("/job")

# //////////////////////////////////////////////////////////////// #
# //////////////////////////////////////////////////////////////// #
# //////////////////////////////////////////////////////////////// #

# Session is the thing that connects to the database and actually moves the data

# this adds data to the database

    new_todo = Todo(
        username = request.username,
        email = request.email,
        
    )
    db.add(new_todo) # -> adds a new user
    db.commit() # -> sends it to the database
    db.refresh(new_user) # -> refreshes the database with the new user data ie. user id
    return new_user
# next week: error handling
# response method
# questions
# github up and working - done

# //////////////////////////////////////////////////////////////// #

jobs = {
    #'JobType': JobType,
}

app2.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app2.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app2.post('/new_job', response_model=mlsSchemas.Job)

def new_job(new_job: mlsSchemas.Job, db: Session = Depends(get_db)):
    new_job_entry = crudmodels.add_new_job(db, new_job)


    return new_job_entry

crudmodels.Base.metadata.create_all(engine)   

@app2.get('/jobs', response_model=List[UserDisplay])
def get_all_jobs(db: Session = Depends(get_db)):
    return crudmodels.get_all_jobs(db)

@app2.get('/job/{id}', response_model=UserDisplay)
def get_job(id: int, db: Session = Depends(get_db)):
    return crudmodels.get_job(db, id)

@app2.get('/job/{id}/bill')
def bill_job(id: int, db: Session = Depends(get_db)):

    job = crudmodels.get_job(db, id)
    return bills(job)

@app2.put('/job/{id}/update')
def update_job(id: int, request: mlsSchemas.Job, db: Session = Depends(get_db)):
    return crudmodels.update_job(db, id, request)

@app2.delete('/job/{id}/delete')
def delete_job(id: int, db: Session = Depends(get_db)):
    return crudmodels.delete_job(db, id)
