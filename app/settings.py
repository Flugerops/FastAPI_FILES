from os import getenv

from dotenv import load_dotenv


load_dotenv()

VT_KEY = getenv("API_KEY")
MAX_FILE_SIZE = 5 * 1024 * 1024
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png"}
ALLOWED_MIME = {"image/jpeg", "image/png"}
TMP_FOLDER = "./tmp"
FILES_FOLDER = "./files"
