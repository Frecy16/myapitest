import requests
import yaml

from test1.datatest.Baseapi import BaseApi


class Testtoken(BaseApi):
    # _corpid = "ww1d0df80a9ad528de"
    # _corpsecret = "8nQMZi5-VPcw1UjYPcOLQWA0g-VdLHNV5531pbIPrkk"
    # res = {
    #     "method": "get",
    #     "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
    #     "params": {
    #         "corpid": _corpid,
    #         "corpsecret": _corpsecret
    #     }
    # }
    def template(self):
        with open("../datatest/testdata.yaml") as f:
            print(f.read())

    def get_token(self):
        # url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        # params = {
        #     "corpid": self._corpid,
        #     "corpsecret": self._corpsecret
        # }
        # r = requests.get(url=url, params=params)
        # # print(r.json()["access_token"])

        req = yaml.safe_load(open("../datatest/testdata.yaml"))
        r = self.requests_http(req)
        return r
        # print(r)

# if __name__ == '__main__':
#     ba = Testtoken()
#     ba.get_token()
