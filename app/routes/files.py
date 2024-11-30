from typing import List

from fastapi import APIRouter, UploadFile, BackgroundTasks, HTTPException

from ..utils import process_file
from ..settings import ALLOWED_EXTENSIONS, ALLOWED_MIME, MAX_FILE_SIZE


files_router = APIRouter(prefix="/file")


@files_router.post("/upload/")
async def upload_files(files: List[UploadFile], background_tasks: BackgroundTasks):
    for file in files:
        if (
            not any(file.filename.lower().endswith(ext) for ext in ALLOWED_EXTENSIONS)
            and file.content_type not in ALLOWED_MIME
        ):
            raise HTTPException(status_code=400, detail="Unsupported file format")

        if file.size > MAX_FILE_SIZE:
            raise HTTPException(status_code=400, detail="File size exceeds the limit.")

        content = await file.read()
        background_tasks.add_task(process_file, file.filename, content)

    return {"message": "Files are being uploaded."}
