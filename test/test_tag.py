import re

import pytest
import requests


# 获取授权token
def get_token():
    # url:https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ID&corpsecret=SECRET
    playload = {
        "corpid": "ww1d0df80a9ad528de",
        "corpsecret": "8nQMZi5-VPcw1UjYPcOLQWA0g-VdLHNV5531pbIPrkk"
    }
    r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken", params=playload)
    return r.json()['access_token']


# 造测试数据
def test_data():
    data = [("测试部" + str(x), x, "管理部" + str(x)) for x in range(6, 16)]
    print(data)
    return data


class Testtag:
    token = get_token()

    # 创建标签
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

    # 获取标签列表
    def test_taglist(self):
        # url=https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token=ACCESS_TOKEN
        # access_token = get_token()
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={self.token}")
        # print(r.json())
        return r.json()

    # 更新标签
    def test_update(self, tagname, tagid):
        # https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token=ACCESS_TOKEN
        body = {
            "tagname": tagname,
            "tagid": tagid
        }
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={self.token}", json=body)
        return r.json()

    # 删除标签
    def test_delete(self, tagid):
        # url = https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token=ACCESS_TOKEN&tagid=TAGID
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={self.token}&tagid={tagid}")
        return r.json()

    # 添加标签成员
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

    # 获取标签成员
    def test_gettaguser(self, tagid):
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token={self.token}&tagid={tagid}")
        return r.json()

    # 删除标签成员接口
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

    # pytest解决多线程执行的问题，需安装pytest-xdist插件，再追加参数 -n auto 指定CPU的数量，auto为系统自动选择
    # 接口集成测试，测试整体接口的功能是否正常，根据是否有对应的业务需求决定是否做接口集成测试
    @pytest.mark.parametrize("tagname,tagid,udpname", test_data())
    def test_integration(self, tagname, tagid, udpname):
        try:
            assert "created" == self.test_create(tagname, tagid)["errmsg"]
        except Exception as e:
            if "invalid tagid" in e.__str__():
                self.test_delete(tagid)
                assert "created" == self.test_create(tagname, tagid)["errmsg"]
        assert tagname == re.findall(f"{tagid}, 'tagname': '(.*?)'", str(self.test_taglist()))[0]
        assert "updated" == self.test_update(udpname, tagid)["errmsg"]
        assert udpname == re.findall(f"{tagid}, 'tagname': '(.*?)'", str(self.test_taglist()))[0]
        assert "ok" == self.test_addtagusers(tagid, ["liuxing"])["errmsg"]
        assert "liuxing" == self.test_gettaguser(tagid)["userlist"][0]["userid"]
        assert "deleted" == self.test_deletetaguser(tagid, ["liuxing"])["errmsg"]
        assert "deleted" == self.test_delete(tagid)["errmsg"]
        # self.test_delete(tagid)
        # print(self.test_taglist())
