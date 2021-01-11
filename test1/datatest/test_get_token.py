from test1.datatest.get_token import Testtoken


class TestGettoken:

    def setup(self):
        self.gettoken = Testtoken()

    def test_get_token(self):
        assert self.gettoken.get_token().json()["errcode"] == 0
