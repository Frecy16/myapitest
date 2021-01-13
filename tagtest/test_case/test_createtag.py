from tagtest import Testtag


class TestCreateTag:
    def test_create1(self):
        # 传入标签名为空，标签创建失败
        assert 40072 == Testtag().test_create("", 5)["errcode"]

    def test_create2(self):
        # 传入32位长度的字母组成的标签名称，标签创建失败
        print(Testtag().test_delete(5))
        assert "created" == Testtag().test_create("aaabbbcccdddeeefffggghhhiiijjjkk", 5)["errmsg"]
        Testtag().test_delete(5)

    def test_create3(self):
        # 传入31位长度的字母组成的标签名称，标签创建成功
        print(Testtag().test_delete(5))
        assert "created" in Testtag().test_create("aaabbbcccdddeeefffggghhhiiijjjk", 5)["errmsg"]
        Testtag().test_delete(5)

    def test_create4(self):
        # 传入31位含特殊字符组成的标签名称，标签创建成功
        assert "tagname exceed max utf8 words 32" in Testtag().test_create("aaabbbcccdddeeeff"
                                                                           "fggghhhiiijjjkkklll1", 5)["errmsg"]

    def test_create5(self):
        # 传入31个汉字组成的标签名称，标签创建成功
        assert "tagname exceed max utf8 words 32" in Testtag().test_create("白日依山尽黄河入海流欲穷千里目更上一层楼"
                                                                           "李白乘舟将欲行忽闻岸上踏歌声", 5)["errmsg"]
