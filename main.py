import csv
from contextlib import asynccontextmanager
from fastapi import FastAPI

def load_data():
    with open("gyul.csv","r") as f:
        reader =csv.DictReader(f,delimiter=",")
        result = {
            int(row.pop("year")):row for row in reader
        } 
    return result

gyl_states ={}

@asynccontextmanager
async def lifespan(app: FastAPI):
    global gyul_stats
    gyul_stats = load_data()
    
    yield
    
app = FastAPI(lifespan=lifespan)    

#app =  FastAPI()

@app.get("/")
async def root():
    return{"message":"Hello, Jeju!"}


@app.get("/stats")
async def get_stats():
    return gyul_stats
    
@app.get("/stats/{year}")
async def get_sigle_year_stats(year: int):
    return gyul_stats[year]


