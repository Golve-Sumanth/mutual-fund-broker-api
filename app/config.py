import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app.db")
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
    RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

settings = Settings()