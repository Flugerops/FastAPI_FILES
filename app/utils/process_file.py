from typing import List
import os

from fastapi import UploadFile, HTTPException
import aiofiles

from ..settings import TMP_FOLDER, FILES_FOLDER
from .antivirus import virus_check
from ..logging import logger
from .image import save_file, optimize_image


async def process_file(filename: str, content: bytes):
    logger.info(f"Checking for viruses in: {filename}")
    virus_result = await virus_check(filename, content)

    if virus_result:
        logger.info(f"Virus check result for {filename}: {virus_result}")
        logger.info(f"Virus file path {filename}")
        if virus_result > 0:

            raise HTTPException(
                status_code=400, detail=f"File contains a virus: {filename}"
            )

    logger.info("File doesn`t contains virus")
    file_location = os.path.join(FILES_FOLDER, filename)

    await save_file(file_location, content)
    await optimize_image(file_location)
