from fastapi import FastAPI
from router import blog_get


app = FastAPI()
# it will default to the first method in the program
# so a method w no parameters should go first
app.include_router(blog_get.router)
@app.get('/hello')
def index ():
    return {'message': 'Hello bob'}


