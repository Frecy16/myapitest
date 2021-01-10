"""
在请求之前，对请求的url进行替换
1、需要二次封装requests，对请求进行定制化；
2、将请求的结构体的url从一个写死的ip地址改为一个（任意的）域名；
3、使用一个env配置文件，存放各个环境的配置信息；
4、然后将请求结果体中的url替换为"env"配置文件中个人选择的url；
5、将env配置文件使用yaml进行管理。
"""
import requests
import yaml


class TestEnv:
    # data = {
    #     "method": "get",
    #     "url": "http://192.168.61.130:9999/testb64.txt",
    #     "headers": {
    #         "req-source": "doclever",
    #         "Content-Type": "application/json"
    #     },
    #     "json": {
    #         "author": "cheny"
    #     }
    # }
    # env = {
    #     "default": "dev",
    #     "req_url": {
    #         "dev": "192.168.61.130",
    #         "test": "127.0.0.1"
    #     }
    # }
    env = yaml.safe_load(open("env.yaml"))

    def send(self, data: dict):
        # 将请求的结构体的url从一个写死的ip地址改为一个（任意的）域名
        data["url"] = str(data["url"]).replace("192.168.61.130", self.env["req_url"][self.env["default"]])
        # 二次封装requests，对请求进行定制化
        r = requests.request(method=data["method"], url=data["url"], headers=data["headers"], json=data["json"])
        return r
