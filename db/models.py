from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from os import getenv
from sqlalchemy import (
    Boolean,
    Interval,
    Time,
    create_engine,
    Integer,
    Column,
    String,
    DateTime,
    ForeignKey,
    Date,
)
from datetime import datetime


URI = getenv("URI")
engine = create_engine(URI)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class FreeDate(Base):
    __tablename__ = "main_freedate"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    free = Column(Boolean)
    now = Column(DateTime)

    def __str__(self):
        return self.date.strftime("%Y-%m-%d %H:%M:%S")


class Service(Base):
    __tablename__ = "main_service"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(String)
    durations = Column(Interval)  # або можна використовувати Interval

    def __str__(self):
        return f"{self.name}: - {self.price} грн."


class Notes(Base):
    __tablename__ = "main_notes"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, index=True)
    name = Column(String)
    username = Column(String)
    time = Column(Time, nullable=True)
    reminder_hours = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    service_id = Column(Integer, ForeignKey("main_service.id"))
    date_id = Column(Integer, ForeignKey("main_freedate.id"))
    free_date = relationship("FreeDate")
    service = relationship("Service")

    def __str__(self):
        return f"Послуга: {self.service.name} | Дата: {self.free_date.date} | Час: {self.time}"


Base.metadata.create_all(bind=engine)