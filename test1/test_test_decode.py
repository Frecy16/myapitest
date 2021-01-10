from test1 import test_decode


class TestApiRequest:
    req_data = {
        "method": "get",
        "url": "http://192.168.61.130:9999/testb64.txt",
        "headers": {
            "req-source": "doclever",
            "Content-Type": "application/json"
        },
        "encoding": "base64"
    }

    def test_send(self):
        result = test_decode.ApiRequest()
        print(result.send(self.req_data))
