import os
from fastapi import FastAPI, HTTPException
from pkg.config.config import Config
from pydantic import BaseModel, ValidationError
from typing import List, Optional
from todo_service.context import ctx
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pkg.model.tasks import Task

import logging
import uvicorn

log = logging.getLogger("todo_service.log")
cfg = Config(os.getenv("CONFIG_PATH"), log)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

class TaskCreate(BaseModel):
    title: str
    description: str = None
    completed: bool = False

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    completed: bool

    class Config:
        from_attributes = True
    
@app.post("/items", response_model=TaskResponse)
async def create_item(item: TaskCreate):
    try:
        task = Task(
            title=item.title,
            description=item.description,
            completed=item.completed
        )

        return ctx.Storage.create(task)
    except Exception as e:
        log.error(f"Error: {e}")
        return JSONResponse(content=jsonable_encoder({"message": "Internal server error"}), status_code=500)

@app.get("/items", response_model=List[TaskResponse])
async def read_items():
    try:
        return ctx.Storage.getTasks()
    except Exception as e:
        log.error(f"Error: {e}")
        return JSONResponse(content=jsonable_encoder({"message": "Internal server error"}), status_code=500)
    
@app.get("/items/{item_id}", response_model=TaskResponse)
async def read_item(item_id: int):
    try:
        task =  ctx.Storage.getByID(item_id)
        if task is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return task
    except HTTPException as e:
        log.info(f"HTTPException occurred: {e.detail}")
        raise e     
    except Exception as e:
        log.error(f"Error: {e}")
        return JSONResponse(content=jsonable_encoder({"message": "Internal server error"}), status_code=500)
    
@app.put("/items/{item_id}", response_model=TaskResponse)
async def update_item(item_id: int, item: TaskCreate):
    try:
        origin_item = ctx.Storage.getByID(item_id)
        if not origin_item:
            raise HTTPException(status_code=404, detail="Item not found")
        
        item_data = item.dict(exclude_unset=True)
        
        for key, value in item_data.items():
            setattr(origin_item, key, value)

        updated_item = ctx.Storage.update(origin_item)

        return updated_item
    except HTTPException as e:
        log.info(f"HTTPException occurred: {e.detail}")
        raise e
    except Exception as e:
        log.error(f"Unexpected error during update_item: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    try:
        if not ctx.Storage.getByID(item_id):
            raise HTTPException(status_code=404, detail="Item not found")
        return ctx.Storage.delete(item_id)
    except HTTPException as e:
        log.info(f"HTTPException occurred: {e.detail}")
        raise e
    except Exception as e:
        log.error(f"Error: {e}")
        return JSONResponse(content=jsonable_encoder({"message": "Internal server error"}), status_code=500)

def main():
    log.info(f"Config: {cfg.host}:{cfg.port}")
    uvicorn.run("todo_service.main:app", host=cfg.host, port=cfg.port, reload=True)
