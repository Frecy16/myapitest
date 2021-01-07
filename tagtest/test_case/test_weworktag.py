from tagtest.api.test_tag import Testtag


class TestWeworkTag:
    def test_create(self):
        print(Testtag().test_create("运维部", 5))

    def test_get_taglist(self):
        print(Testtag().test_taglist())

    def test_updatetag(self):
        print(Testtag().test_update("人力资源部", 5))

    def test_deletetag(self):
        print(Testtag().test_delete(5))

    def test_addtagusers(self):
        print(Testtag().test_addtagusers(5, ["liuxing", "angler1"]))

    def test_gettagusers(self):
        print(Testtag().test_gettaguser(5))

    def test_deletetaguser(self):
        print(Testtag().test_deletetaguser(5, ["liuxing", "angler1"]))
