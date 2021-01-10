import json
import requests
import base64


# def test_encode():
#     url = "http://192.168.61.130:9999/testb64.txt"
#     r = requests.get(url=url)
#     res = json.loads(base64.b64decode(r.content))
#     print(res)
class ApiRequest:

    def send(self, data: dict):
        r = requests.request(data["method"], data["url"], headers=data["headers"])
        if data["encoding"] == "base64":
            return json.loads(base64.b64decode(r.content))
        ## 把加密过后的响应值发给第三方服务，让第三方去做解密，然后返回解密过后的信息
        elif data["encoding"] == "ASE":
            return requests.post("url", data=r.content)
        elif data["encoding"] == "MD5":
            return "MD5 is used for decoding."
