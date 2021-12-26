from pathlib import Path

from sqlmodel import Session, create_engine, SQLModel

_sqlite_filename = "data/database.sqlite3"
_sqlite_url = f"sqlite:///{_sqlite_filename}"

Path(_sqlite_filename).unlink(missing_ok=True)
_engine = create_engine(
    _sqlite_url, echo=False, connect_args=dict(check_same_thread=False)
)


def create_db_and_tables():
    SQLModel.metadata.create_all(_engine)


def session():
    with Session(_engine) as s:
        yield s
