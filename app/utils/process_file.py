from typing import List
import os

from fastapi import UploadFile, HTTPException
import aiofiles

from ..settings import TMP_FOLDER
from .antivirus import virus_check


async def process_file(filename: str, content: bytes):
    file_location = os.path.join(TMP_FOLDER, filename)
    async with aiofiles.open(file_location, "wb") as out_file:
        await out_file.write(content)

    virus_result = await virus_check(file_location)
    if virus_result:
        print(virus_result)

    # if virus_result:
    #     print(virus_result)
    # os.remove(file_location)
    # raise HTTPException(
    #     status_code=400, detail=f"File contains a virus: {file.filename}"
    # )

    # await optimize_image(file_path)
    # await move_file_to_uploads(file_path)
