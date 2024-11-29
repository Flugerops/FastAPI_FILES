import aiohttp
import aiofiles

from ..settings import VT_KEY


async def virus_check(file_path: str) -> dict:
    url = "https://www.virustotal.com/api/v3/files"
    headers = {
        "accept": "application/json",
        "x-apikey": VT_KEY,
    }
    async with aiohttp.ClientSession() as session:
        async with aiofiles.open(file_path, "rb") as file:
            async with session.post(
                url, data={"file": file}, headers=headers
            ) as response:
                analyse_id = await response.json()
                result_url = (
                    f"https://www.virustotal.com/api/v3/analyses/{analyse_id.get("id")}"
                )
            async with session.get(result_url, headers=headers):
                return response.json()
