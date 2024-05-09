from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Gestión Studio DL"
    PROJECT_VERSION: str = "1.0"
    PROJECT_DESCRIPTION: str = "Una aplicación para la gestión de estudios de modelos webcam."

    class Config:
        case_sensitive = True

settings = Settings()