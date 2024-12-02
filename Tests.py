import os

import pytest
from httpx import ASGITransport, AsyncClient
from PIL import Image
import aiofiles

from app import app
from app.settings import ALLOWED_EXTENSIONS, ALLOWED_MIME, MAX_FILE_SIZE


@pytest.mark.asyncio
async def test_upload_files_success():
    test_file_path = "test_image.jpg"
    image = Image.new("RGB", (100, 100), color=(73, 109, 137))
    image.save(test_file_path, "JPEG")

    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        with open(test_file_path, "rb") as buffer:
            response = await ac.post(
                "/file/upload/",
                files={"files": (test_file_path, buffer, "image/jpeg")},
            )

    assert response.status_code == 200

    os.remove(test_file_path)


@pytest.mark.asyncio
async def test_upload_files_unsupported_format():
    test_file_path = "test_file.txt"
    with open(test_file_path, "wb") as buffer:
        buffer.write(b"This is a test file.")

    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        with open(test_file_path, "rb") as buffer:
            response = await ac.post(
                "/file/upload/",
                files={"files": (test_file_path, buffer)},
            )
    assert response.status_code == 400

    os.remove(test_file_path)


@pytest.mark.asyncio
async def test_upload_files_exceeds_size():
    test_file_path = "large_file.jpg"
    image = Image.new("RGB", (20000, 20000), color=(73, 109, 137))
    image.save(test_file_path, "JPEG")

    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        with open(test_file_path, "rb") as buffer:
            response = await ac.post(
                "/file/upload/",
                files={"files": (test_file_path, buffer, "image/jpeg")},
            )

    assert response.status_code == 400

    os.remove(test_file_path)
