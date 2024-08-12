from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DISCORD_TOKEN: str
    DISCORD_CLIENT_ID: str
    OWNER_ID: str
    TEST_GUILD: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
