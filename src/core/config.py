from pydantic import BaseSettings


class Settings(BaseSettings):
    SERVER_HOST: str = '127.0.0.1'
    SERVER_PORT: int = 8000
    PG_DATABASE_URL: str = "postgresql://api_mpc:api_mpc_pwd@localhost:54321/api_mpc_db"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    ALGORITHM: str = "HS256"
    # Below default key or "openssl rand -hex 32".
    SECRET_KEY: str = "08d026286c19e9a35cc64a21f4aa46338ca076da55c285a6492964d894da50e6"


settings = Settings(
    _env_file='../.env',
    _env_file_encoding='utf-8',
)