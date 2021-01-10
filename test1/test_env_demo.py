from test1 import env_demo


class TestEnv:
    data = {
        "method": "get",
        "url": "http://192.168.61.130:9999/testb64.txt",
        "headers": {
            "req-source": "doclever",
            "Content-Type": "application/json"
        },
        "json": {
            "author": "cheny"
        }
    }

    def test_send(self):
        result = env_demo.TestEnv()
        print(result.send(self.data).text)
