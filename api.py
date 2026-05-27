from http.client import HTTPException

import uvicorn
from fastapi import FastAPI, HTTPException
from db import database, db_methods
from sqlalchemy import Table

app = FastAPI()
detectives_table = Table('Detective', database.metadata_obj, autoload_with=database.engine)
locations_table = Table('Location', database.metadata_obj, autoload_with=database.engine)

@app.get('/detectives')
async def get_detectives():
    return db_methods.get_detectives(detectives_table), 200

@app.get('/locations')
async def get_locations():
    return db_methods.get_locations(locations_table), 200

@app.put('/detectives/{detective_id}')
async def create_detective(name, clue_count, location_id):
    try:
        db_methods.insert_detective(detectives_table, name,clue_count,location_id)
        return {'detective name': name, 'clue count': clue_count}, 201
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == '__main__':
    uvicorn.run('api:app', reload=True)