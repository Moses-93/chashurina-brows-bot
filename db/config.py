from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
from os import getenv

load_dotenv()
URI = getenv("URI")
engine = create_async_engine(URI)
Session = async_sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)
async_session = Session
Base = declarative_base()
