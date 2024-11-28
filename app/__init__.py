from os import getenv, makedirs

from fastapi import FastAPI
from dotenv import load_dotenv


load_dotenv()
app = FastAPI()

VT_KEY = getenv("API_KEY")
MAX_FILE_SIZE = 5 * 1024 * 1024
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png"}
TMP_FOLDER = "./tmp"

makedirs(TMP_FOLDER, exist_ok=True)
