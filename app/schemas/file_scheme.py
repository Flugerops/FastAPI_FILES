from fastapi import UploadFile, HTTPException
from pydantic import BaseModel, field_validator
import aiofiles

from .. import ALLOWED_EXTENSIONS, MAX_FILE_SIZE, TMP_FOLDER


class FileScheme(BaseModel):
    file: UploadFile

    @field_validator("file")
    @classmethod
    async def checksize_ext(cls, file: UploadFile):
        if not any(file.filename.lower().endswith(ext) for ext in ALLOWED_EXTENSIONS):
            raise HTTPException(status_code=400, detail="Unsupported file format")

        if file.size > MAX_FILE_SIZE:
            raise HTTPException(status_code=400, detail="File size exceeds the limit.")


#         file_path = f"{TMP_FOLDER}/temp_{file.filename}"
#         async with aiofiles.open(file_path, "wb") as temp_file:
#             content = await file.read()
#             await temp_file.write(content)
