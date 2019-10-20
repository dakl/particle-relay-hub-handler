import httpx
#from requests import post

import structlog
logger = structlog.getLogger(__name__)

class PostRequestFactory:
    async def create(self, url, payload, headers=None):
        if not headers:
            headers = {}
        response = await httpx.post(url, data=payload, headers=headers)
        logger.info('API Responed', status=response.status_code)
        return response.json()
