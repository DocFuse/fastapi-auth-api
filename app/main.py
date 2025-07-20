from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.api.v1 import users

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Auth System")

app.include_router(users.router, prefix="/api/v1", tags=["users"])

@app.get("/")
def root():
    return {"message": "欢迎来到 FastAPI 中型项目模板"}
