from pydantic import BaseSettings


class Settings(BaseSettings):
    # Postgres
    PG_DATABASE_URL: str = "postgresql://api_mpc:api_mpc_pwd@localhost:54321/api_mpc_db"

    # App
    SERVER_HOST: str = '127.0.0.1'
    SERVER_PORT: int = 8000


settings = Settings(
    _env_file='../.env',
    _env_file_encoding='utf-8',
)
