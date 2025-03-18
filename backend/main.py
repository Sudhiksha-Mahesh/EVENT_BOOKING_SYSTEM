from fastapi import FastAPI
from .database import engine, Base
from .routes import users, events, bookings

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(users.router)
app.include_router(events.router)
app.include_router(bookings.router)