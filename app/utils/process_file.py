from typing import List
import os

from fastapi import UploadFile, HTTPException
import aiofiles

from .. import TMP_FOLDER
from .antivirus import virus_check


async def process_file(file: UploadFile):
    file_location = os.path.join(TMP_FOLDER, file.filename)
    async with aiofiles.open(file_location, "wb") as out_file:
        content = await file.read()
        await out_file.write(content)

    virus_result = await virus_check(file_location)

    if virus_result:
        print(virus_result)
        # os.remove(file_location)
        # raise HTTPException(
        #     status_code=400, detail=f"File contains a virus: {file.filename}"
        # )

    # await optimize_image(file_path)
    # await move_file_to_uploads(file_path)
