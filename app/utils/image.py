import aiofiles

from PIL import Image

from ..logging import logger


async def save_file(file_path: str, content: bytes):
    async with aiofiles.open(file_path, "wb") as buffer:
        await buffer.write(content)
    logger.info(f"File saved: {file_path}")


async def optimize_image(file_path: str):
    logger.info(f"Optimizing image: {file_path}")
    try:
        with Image.open(file_path) as img:
            img.thumbnail((800, 800))
            img.save(file_path, optimize=True, quality=85)

        logger.info(f"Image optimized and saved as: {file_path}")

    except Exception as e:
        logger.error(f"Error optimizing image {file_path}: {e}")
