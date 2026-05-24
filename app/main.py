from fastapi import FastAPI
from app.routes.rag_routes import router

app = FastAPI()

@app.get("/")
def home():
    return {"message": "RAG API is running!"}

app.include_router(router)