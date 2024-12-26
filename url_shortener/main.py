import os
from fastapi import FastAPI
from pkg.config.config import Config
from fastapi.middleware.cors import CORSMiddleware
import logging
from url_shortener.context import ctx
import uvicorn
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import hashlib
from pkg.model.urls import ShortURL


log = logging.getLogger("url_shortener.log")
cfg = Config(os.getenv("CONFIG_PATH"), log)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.post("/shorten", response_model=dict)
async def shorten(body: dict):
    try:
        url = body.get("url")
        if not url:
            return JSONResponse(content=jsonable_encoder({"message": "url is required"}), status_code=400)
        short_id = hashlib.md5(url.encode()).hexdigest()[:8]
        ctx.Storage.save(ShortURL(original_url=url, short_id=short_id))
        return {"short_url": short_id}
    except Exception as e:
        log.error(f"Error: {e}")
        return JSONResponse(content=jsonable_encoder({"message": "Internal server error"}), status_code=500)

@app.get("/{short_id}")
async def redirect(short_id: str):
    try:
        url = ctx.Storage.get(short_id)
        return {"url": url.original_url}
    except Exception as e:
        log.error(f"Error: {e}")
        return JSONResponse(content=jsonable_encoder({"message": "Internal server error"}), status_code=500)
    
@app.get("/stats/{short_id}")
async def stats(short_id: str):
    try:
        return ctx.Storage.get(short_id)
    except Exception as e:
        log.error(f"Error: {e}")
        return JSONResponse(content=jsonable_encoder({"message": "Internal server error"}), status_code=500)

def main():
    log.info(f"Service: {cfg.service_name} is starting at {cfg.host}:{cfg.port}")
    uvicorn.run("url_shortener.main:app", host=cfg.host, port=cfg.port, reload=True)
