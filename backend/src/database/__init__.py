from sqlmodel import create_engine
from .config import DATABASE_URL

# Create database engine
engine = create_engine(DATABASE_URL, echo=True)