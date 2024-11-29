from os import getenv, makedirs

from fastapi import FastAPI
from dotenv import load_dotenv

from .routes import files_router


load_dotenv()
app = FastAPI()

VT_KEY = getenv("API_KEY")
MAX_FILE_SIZE = 5 * 1024 * 1024
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png"}
ALLOWED_MIME = {"image/jpeg", "image/png"}
TMP_FOLDER = "./tmp"
FILES_FOLDER = "./files"

app.include_router(files_router)

makedirs(TMP_FOLDER, exist_ok=True)
makedirs(FILES_FOLDER, exist_ok=True)
