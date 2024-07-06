from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str
    password: str

class UserDisplay(BaseModel):
    username: str
    email: str
    class Config():
        orm_mode = True 
        # allows the system to return database data into this format
        # converts databse data into user display data ie DBUser to UserDisplay