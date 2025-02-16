import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 1440))
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

HOST=os.getenv("HOST")
PORT=os.getenv("PORT")