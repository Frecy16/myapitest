from tagtest import Testtag


class TestWeworkTag:
    def test_create(self):
        print(Testtag().test_create("运维部", 5))

    def test_get_taglist(self):
        print(Testtag().test_taglist())

    def test_updatetag(self):
        print(Testtag().test_update("人力资源部", 5))

    def test_deletetag(self):
        assert "deleted" == Testtag().test_delete(5)["errmsg"]

    def test_addtagusers(self):
        print(Testtag().test_addtagusers(5, "liuxing"))

    def test_gettagusers(self):
        print(Testtag().test_gettagusers(5))

    def test_deletetagusers(self):
        print(Testtag().test_deletetagusers(5, "liuxing"))
