from sqlalchemy import Column, Integer, Boolean, ForeignKey, String
from sqlalchemy.orm import Session, relationship 
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import func



Base = declarative_base()


class JobCounter(Base):
    __tablename__ = 'job_count'
    id = Column(Integer, primary_key=True, index=True)
    count = Column(Integer, default=0)

class DBJob(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True, index=True)
    jobtype_id = Column(String, ForeignKey('job_types.id'))
    jobtype = relationship("DBJobType")
    jobcount = Column(Integer)
    date = Column(String)
    starttime = Column(Integer)
    stoptime = Column(Integer)
    travel = Column(Integer)
    rate = Column(Integer)
    number_of_movers = Column(Integer)
    mileage = Column(Integer)

    class DBJobType(Base):
        __tablename__ = "job_types"
        id = Column(Integer, primary_key=True, index=True)
        loadSwap = Column(Boolean)
        uhaul = Column(Boolean)
        fullService = Column(Boolean)
        other = Column(Boolean)

# adds counter to the database
def get_job_counter(db: Session):
    count = db.query(JobCounter).first()
    if not count:
        count = JobCounter(job_count=0)
        db.add(count)
        db.commit()
    return count    

# def get_job_counter(db: Session):
    # return db.query(JobCounter).first()


def increment_job_counter(db: Session) -> int:
    count = db.query(JobCounter).with_for_update().first()
    count += 1
    db.commit()
    return count

def generate_id(count: int):
    today = datetime.today().date()
    id = f'{today}-{count}'
    return id

# this adds data to the database
def add_new_job(db: Session, request: DBJob):
    new_job = DBJob(
        id = 
        generate_id(),
        jobtype_id = request.jobtype_id,
        date = request.id,
        starttime = request.starttime,
        stoptime = request.stoptime,
        travel = request.travel,
        rate = request.rate,
        number_of_movers = request.number_of_movers,
        mileage = request.mileage

    )
    db.add(new_job) # -> adds a new user
    db.commit() # -> sends it to the database
    db.refresh(new_job) # -> refreshes the database with the new user data ie. user id
    return new_job