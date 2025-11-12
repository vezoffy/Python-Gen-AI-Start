from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///accounts.db"

engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
Base = declarative_base()


def init_db():
    """Create all tables. Imports models so that Base.metadata is populated."""
    # Import models here to ensure they are registered on Base.metadata
    import models  # noqa: F401
    Base.metadata.create_all(bind=engine)


def get_session():
    return SessionLocal()
