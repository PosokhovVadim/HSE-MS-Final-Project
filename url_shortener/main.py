import os
from fastapi import FastAPI
from pkg.Config.config import Config
from fastapi.middleware.cors import CORSMiddleware
import logging
# from todo_service.context import ctx
import uvicorn
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

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

@app.get("/")
async def root():
    return {"message": "Hello World"}

def main():
    log.info(f"Config: {cfg.host}:{cfg.port}")
    uvicorn.run("todo_service.main:app", host=cfg.host, port=cfg.port, reload=True)
