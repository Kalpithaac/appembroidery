from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    azure_blob_conn: str
    azure_blob_container: str

    azure_cv_endpoint: str
    azure_cv_key: str

    default_kmeans_colors: int = 6

    class Config:
        env_file = ".env"

settings = Settings()