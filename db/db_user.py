from db.hash import Hash
from sqlalchemy.orm import Session
from schemas import UserBase
from db.models import DBUser

# Session is the thing that connects to the database and actually moves the data

# this adds data to the database
def create_user(db: Session, request: UserBase):
    new_user = DBUser(
        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )
    db.add(new_user) # -> adds a new user
    db.commit() # -> sends it to the database
    db.refresh(new_user) # -> refreshes the database with the new user data ie. user id
    return new_user

# this gets all users from the database
# input is Session object 
# querys the database for all DBUser objects

def get_all_users(db: Session):
    return db.query(DBUser).all()

# gets a specific user by id
def get_user(db: Session, id: int):
    return db.query(DBUser).filter(DBUser.id == id).first()

def update_user(db: Session, id: int, request: UserBase):
    user = db.query(DBUser).filter(DBUser.id == id).first()
    user.update({
        DBUser.username: request.username,
        DBUser.email: request.email,
        DBUser.password: Hash.bcrypt(request.password)
    })