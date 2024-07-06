from pydantic import BaseModel




print("hello, world")

class JobType(BaseModel):
    uhaul: bool = False
    loadswap: bool = False
    unload: bool = False
    fullService: bool = False


class Job(BaseModel):

    jobtype: JobType
    date: int
    starttime: int
    stoptime: int
    travel: int
    rate: int
    number_of_movers: int
    mileage: int



    

def bill(starttime, stoptime, travel, rate, mileage):
    job_time = (stoptime - starttime) + travel
    fuel = mileage * .25
    total = job_time * rate + fuel
    return total


