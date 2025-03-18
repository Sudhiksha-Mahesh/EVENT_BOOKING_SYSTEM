from sqlalchemy.orm import Session
from . import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "hashed"
    db_user = models.User(username=user.username, email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_event(db: Session, event: schemas.EventCreate):
    db_event = models.Event(name=event.name, date=event.date, location=event.location)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

def create_booking(db: Session, booking: schemas.BookingCreate):
    db_booking = models.Booking(user_id=booking.user_id, event_id=booking.event_id)
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

