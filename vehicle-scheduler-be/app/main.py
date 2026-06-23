from fastapi import FastAPI
from routes import router

app = FastAPI(
    title="Vehicle Scheduler API"
)

app.include_router(router)


@app.get("/")
async def home():
    return {
        "message": "Vehicle Scheduler API Running"
    }