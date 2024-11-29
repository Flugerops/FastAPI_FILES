from typing import List

from fastapi import APIRouter, UploadFile, BackgroundTasks

from ..utils import process_file


files_router = APIRouter(prefix="file")


@files_router.post("/upload/")
async def upload_files(files: List[UploadFile], background_tasks: BackgroundTasks):
    for file in files.files:
        background_tasks.add_task(process_file, file)

    return {"message": "Files are being uploaded."}
