from databases import Database
from sqlalchemy import create_engine, MetaData
from core.config import settings

databases = Database(settings.PG_DATABASE_URL)

metadata = MetaData()
engine = create_engine(settings.PG_DATABASE_URL)

