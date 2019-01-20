from requests import post


class PostRequestFactory:
    def create(self, url, payload, headers=None):
        if not headers:
            headers = {}
        return post(url, data=payload, headers=headers).json()
