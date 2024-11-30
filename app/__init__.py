from os import getenv, makedirs

from fastapi import FastAPI
from dotenv import load_dotenv

from .routes import files_router


app = FastAPI()


app.include_router(files_router)

from .settings import TMP_FOLDER, FILES_FOLDER


makedirs(TMP_FOLDER, exist_ok=True)
makedirs(FILES_FOLDER, exist_ok=True)
