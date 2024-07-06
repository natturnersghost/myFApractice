from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI, Depends
from crud.MLS import mlsSchemas
from datetime import datetime
from sqlalchemy.orm import Session
from db.database import get_db
from crud import crudmodels

app1 = FastAPI()
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

 
@app1.post('/new_job', response_model=mlsSchemas.Job)

def new_job(new_job: mlsSchemas.Job, db: Session = Depends(get_db)):
    count = crudmodels.get_job_counter(db)
    count = crudmodels.increment_job_counter(db)
    job_id = crudmodels.generate_id(count)
    
    return crudmodels.add_new_job(db, new_job),{
                'job_id': job_id,
                'new_job': new_job,
            }

    