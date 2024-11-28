import aiohttp

from .. import VT_KEY


async def virus_check(file_path: str) -> dict:
    url = "https://www.virustotal.com/api/v3/files"
    headers = {
        "accept": "application/json",
        "x-apikey": VT_KEY,
    }
    async with aiohttp.ClientSession() as session:
        with open(file_path, "rb") as file:
            async with session.post(
                url, data={"file": file}, headers=headers
            ) as response:
                return await response.json()
