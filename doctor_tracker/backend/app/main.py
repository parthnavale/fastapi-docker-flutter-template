from fastapi import FastAPI
from app.routes import example_router  # create a router later

app = FastAPI()

app.include_router(example_router, prefix="/api")

