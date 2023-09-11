from fastapi import FastAPI, Request
import uvicorn
import os
from dotenv import load_dotenv

from src.routes.chat import chat

load_dotenv()

app = FastAPI()
app.include_router(chat)


@app.get("/healthcheck")
async def root():
    return {"msg": "API is online"}


if __name__ == "__main__":
    if os.environ.get("APP_ENV") == "development":
        uvicorn.run("main:app", port=3500, workers=4, reload=True)
    else:
        pass
