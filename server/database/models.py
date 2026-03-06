from sqlalchemy import *

engine = create_engine("sqlite:///radio.db")
metadata = MetaData()

songs = Table(
    "songs",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String),
    Column("artist", String),
    Column("path", String)
)

metadata.create_all(engine)