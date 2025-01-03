from .config import Base
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Boolean,
    Interval,
    Time,
    Integer,
    Column,
    String,
    DateTime,
    ForeignKey,
    Date,
)


class Dates(Base):
    __tablename__ = "main_dates"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    free = Column(Boolean, default=True, index=True)
    del_time = Column(DateTime, nullable=False)

    def __str__(self):
        return self.date.strftime("%Y-%m-%d %H:%M:%S")


class Services(Base):
    __tablename__ = "main_services"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    durations = Column(Interval, nullable=False)

    def __str__(self):
        return f"{self.name}: - {self.price} грн."


class Notes(Base):
    __tablename__ = "main_notes"
    id = Column(Integer, primary_key=True)
    active = Column(Boolean, default=True, index=True)
    user_id = Column(Integer, index=True, nullable=False)
    name = Column(String, nullable=False)
    username = Column(String)
    time = Column(Time, nullable=False)
    service_id = Column(Integer, ForeignKey("main_services.id", ondelete="CASCADE"))
    date_id = Column(Integer, ForeignKey("main_dates.id", ondelete="CASCADE"))
    reminder_hours = Column(Integer, nullable=True)
    created_at = Column(DateTime)
    date = relationship("Dates")
    service = relationship("Services")

    def __str__(self):
        return (
            f"Послуга: {self.service.name} | Дата: {self.date.date} | Час: {self.time}"
        )
