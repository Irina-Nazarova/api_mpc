import sqlalchemy

from .base import metadata

devices = sqlalchemy.Table(
    "devices",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("ip_address", sqlalchemy.String),
    sqlalchemy.Column("hostname", sqlalchemy.String),
    sqlalchemy.Column("model", sqlalchemy.String),
)