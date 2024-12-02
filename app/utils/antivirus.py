import aiohttp
import aiofiles

from ..settings import VT_KEY

import aiohttp
import aiofiles

from ..settings import VT_KEY
from ..logging import logger


async def virus_check(filename: str, content: bytes) -> dict:
    url = "https://www.virustotal.com/api/v3/files"
    headers = {
        "accept": "application/json",
        "x-apikey": VT_KEY,
    }
    async with aiohttp.ClientSession() as session:
        form = aiohttp.FormData()
        form.add_field("file", content, filename=filename, content_type="image/png")

        async with session.post(url, data=form, headers=headers) as response:
            analyse_id = await response.json()
            result_url = f"https://www.virustotal.com/api/v3/analyses/{analyse_id.get('data').get('id')}"
            async with session.get(result_url, headers=headers) as result_response:
                response_result = await result_response.json()
                logger.info(f"{response_result}")
                malicious_count = (
                    response_result.get("data")
                    .get("attributes")
                    .get("stats")
                    .get("malicious")
                )
                logger.info(f"Malicious count {malicious_count}")
                return malicious_count
