from fastapi import FastAPI

from config.config import initiate_database
from routes.document import router as DocumentRouter
from routes.document import router as TrendRouter

app = FastAPI()


@app.on_event("startup")
async def start_database():
    await initiate_database()


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app."}


app.include_router(DocumentRouter, tags=["Documents"])
app.include_router(TrendRouter, tags=["Trends"])
