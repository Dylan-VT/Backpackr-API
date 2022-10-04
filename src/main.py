"""
Main API for Backpackr.
Started 10/3/2022
"""
import certifi
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from motor import motor_asyncio
from dotenv import dotenv_values


from locations import Country

#read in dotenv
cfg = dotenv_values("../.env")

#force TLS cert
ca = certifi.where()

#connect to mongo
client = motor_asyncio.AsyncIOMotorClient(cfg["mongo_connection_string"],
                                            tls = True,
                                            tlsCAFile = ca)
db = client['Backpackr']

app = FastAPI()


@app.get("/")
def read_root():
    """
    Ping the root
    """
    return {"Hello": "World"}


@app.post("/create/country", response_model = Country)
async def create_country(country: Country):
    """
    Endpoint to create a new country
    """
    #encode country as dict
    country = jsonable_encoder(country)
  
    #insert country and grab new country to return
    new_country = await db['countries'].insert_one(country)
    created_country = await db['countries'].find_one({"_id": new_country.inserted_id})
    
    return JSONResponse(status_code = status.HTTP_201_CREATED, content = created_country)
