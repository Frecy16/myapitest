import requests


class BaseApi:
    def requests_http(self, data):
        r = requests.request(**data)
        return r
