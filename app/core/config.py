from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8"
    )
    APP_NAME: str = "Chat"
    OPENAI_API_KEY: str
    MODEL: str = "gpt-5-nano"
    STORE_BACKEND: str = "memory"


settings = Settings()
