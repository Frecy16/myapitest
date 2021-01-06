import pytest
import requests


def get_token():
    # url:https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ID&corpsecret=SECRET
    playload = {
        "corpid": "ww1d0df80a9ad528de",
        "corpsecret": "8nQMZi5-VPcw1UjYPcOLQWA0g-VdLHNV5531pbIPrkk"
    }
    r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken", params=playload)
    return r.json()['access_token']


def test_data():
    data = [("测试部" + str(x), x) for x in range(6, 16)]
    print(data)
    return data


class Testtag:
    token = get_token()

    def test_create(self, tagname, tagid):
        """
        url: https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token=ACCESS_TOKEN
        """
        # access_token = get_token()
        body = {
            "tagname": tagname,
            "tagid": tagid
        }
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={self.token}", json=body)
        print(r.json())
        return r.json()

    def test_taglist(self):
        # url=https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token=ACCESS_TOKEN
        # access_token = get_token()
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={self.token}")
        # print(r.json())
        # return r.json()["taglist"]
        return r.json()

    def test_get(self, tagid):
        # url = https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token=ACCESS_TOKEN&tagid=TAGID
        # access_token = get_token()
        # tagid = self.test_taglist()[0]["tagid"]
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token={self.token}&tagid={tagid}")
        return r.json()

    def test_update(self, tagname, tagid):
        # https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token=ACCESS_TOKEN
        # access_token = get_token()
        body = {
            "tagname": tagname,
            "tagid": tagid
        }
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={self.token}", json=body)
        return r.json()

    def test_delete(self, tagid):
        # url = https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token=ACCESS_TOKEN&tagid=TAGID
        # access_token = get_token()
        # tagid = 4
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={self.token}&tagid={tagid}")
        return r.json()

    def test_addtagusers(self, tagid, userlist, partylist=None):
        # url = https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers?access_token=ACCESS_TOKEN
        # access_token = get_token()
        if partylist is None:
            partylist = [4]
        body = {
            "tagid": tagid,
            "userlist": userlist,
            "partylist": partylist
        }
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers?access_token={self.token}", json=body)
        return r.json()

    def test_gettaguser(self, tagid):
        # access_token = get_token()
        # tagid = 1
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token={self.token}&tagid={tagid}")
        return r.json()

    def test_deletetaguser(self, tagid, userlist, partylist=None):
        # access_token = get_token()
        if partylist is None:
            partylist = [1]
        body = {
            "tagid": tagid,
            "userlist": userlist,
            "partylist": partylist
        }
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/tag/deltagusers?access_token={self.token}", json=body)
        return r.json()

    @pytest.mark.parametrize("tagname,tagid", test_data())
    def test_integration(self, tagname, tagid):
        try:
            assert "created" == self.test_create(tagname, tagid)["errmsg"]
        except Exception as e:
            if "invalid tagid" in e.__str__():
                self.test_delete(tagid)
                assert "created" == self.test_create(tagname, tagid)["errmsg"]
        # print(tagname, type(tagname), tagid, type(tagid))
        # self.test_create(tagname, tagid)
        assert {"tagid":tagid,"tagname":tagname} == self.test_taglist()["taglist"][-1]
        assert "updated" == self.test_update("管理部", tagid)["errmsg"]
        assert "管理部" in self.test_taglist()["taglist"][-1]["tagname"]
        assert "ok"  == self.test_addtagusers(tagid, ["liuxing"])["errmsg"]
        assert "liuxing" == self.test_gettaguser(tagid)["userlist"][0]["userid"]
        # print(self.test_gettaguser(tagid)["userlist"][-1]["userid"])
        assert "deleted" == self.test_deletetaguser(tagid, ["userlist"])["errmsg"]
        assert "deleted" == self.test_delete(tagid)["errmsg"]
