from typing import List

from fastapi import UploadFile, HTTPException
from pydantic import BaseModel, field_validator
import aiofiles

from .. import ALLOWED_EXTENSIONS, MAX_FILE_SIZE, TMP_FOLDER, ALLOWED_MIME


class FileScheme(BaseModel):
    files: List[UploadFile]

    @field_validator("files")
    @classmethod
    async def checksize_ext(cls, files: UploadFile):
        for file in files:

            if (
                not any(
                    file.filename.lower().endswith(ext) for ext in ALLOWED_EXTENSIONS
                )
                and file.content_type not in ALLOWED_MIME
            ):
                raise HTTPException(status_code=400, detail="Unsupported file format")

            if file.size > MAX_FILE_SIZE:
                raise HTTPException(
                    status_code=400, detail="File size exceeds the limit."
                )

        return file
