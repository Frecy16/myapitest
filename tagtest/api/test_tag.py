import requests
from tagtest.api.util import Util


class Testtag:
    def __init__(self):
        self.token = Util().get_token()

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
