from pathlib import Path

import sqlmodel as sm

sqlite_filename = "data/database.db"
sqlite_url = f"sqlite:///{sqlite_filename}"

Path(sqlite_filename).unlink(missing_ok=True)
engine = sm.create_engine(
    sqlite_url, echo=False, connect_args=dict(check_same_thread=False)
)


def create_db_and_tables():
    sm.SQLModel.metadata.create_all(engine)


def get_session():
    with sm.Session(engine) as session:
        yield session
