
from fastapi import FastAPI
from routers.categories import router as categories_router

app = FastAPI(
    title="Online Recipe Book API",
    description="An API for managing recipes and categories",
    version="1.0.0"
)

app.include_router(categories_router)


@app.get("/")
def home():
    return {"message": "Welcome to Online Recipe Book API"}
