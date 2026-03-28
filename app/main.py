from fastapi import FastAPI
from app.db.database import engine, Base
from app.models import user
from app.routes import auth, protected
from app.models import task
from app.routes import tasks

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(protected.router)
app.include_router(tasks.router)

@app.get("/")
def root():
    return {"message": "API is running"}