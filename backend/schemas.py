from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        from_attributes = True

class EventBase(BaseModel):
    name: str
    date: datetime
    location: str

class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: int

    class Config:
        from_attributes = True

class BookingBase(BaseModel):
    user_id: int
    event_id: int

class BookingCreate(BookingBase):
    pass

class Booking(BookingBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True

