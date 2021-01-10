import json
import yaml
import requests


def openfile(filepath="../api/test_data.yaml"):
    with open(filepath, 'r', encoding="utf-8") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return data


class BaseApi:
    params = {}

    def send(self, data):
        raw_data = json.dumps(data)
        for key, value in self.params.items():
            value = str(value)
            raw_data = raw_data.replace("${" + key + "}", value)
        data = json.loads(raw_data)
        return requests.request(**data).json()
