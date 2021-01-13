from tagtest import BaseApi, openfile
from tagtest import Util


# 标签类，继承基础接口类，便于调用其方法及参数
class Testtag(BaseApi):
    def __init__(self):
        self.token = Util().get_token()
        self.params["token"] = Util().get_token()

    # 创建标签
    def test_create(self, tagname, tagid):
        """
        url: https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token=ACCESS_TOKEN
        """
        self.params["tagname"] = tagname
        self.params["tagid"] = tagid
        data = openfile()
        # r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={self.token}", json=data)
        # print(r.json())
        return self.send(data["create"])
        # return BaseApi().send(data["create"])

    # 获取标签列表
    def test_taglist(self):
        # url=https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token=ACCESS_TOKEN
        # r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={self.token}")
        data = openfile()
        return self.send(data["taglist"])

    # 更新标签
    def test_update(self, tagname, tagid):
        # https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token=ACCESS_TOKEN
        # body = {
        #     "tagname": tagname,
        #     "tagid": tagid
        # }
        # r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={self.token}", json=body)
        self.params["tagname"] = tagname
        self.params["tagid"] = tagid
        data = openfile()
        return self.send(data["update"])

    # 删除标签
    def test_delete(self, tagid):
        # url = https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token=ACCESS_TOKEN&tagid=TAGID
        # r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={self.token}&tagid={tagid}")
        self.params["tagid"] = tagid
        data = openfile()
        return self.send(data["delete"])

    # 添加标签成员
    def test_addtagusers(self, tagid, userlist, partylist=None):
        # url = https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers?access_token=ACCESS_TOKEN
        # access_token = get_token()
        if partylist is None:
            partylist = "4"
        # body = {
        #     "tagid": tagid,
        #     "userlist": userlist,
        #     "partylist": partylist
        # }
        # r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers?access_token={self.token}", json=body)
        self.params["tagid"] = tagid
        self.params["userlist"] = userlist
        self.params["partylist"] = partylist
        data = openfile()
        return self.send(data["addtagusers"])

    # 获取标签成员
    def test_gettagusers(self, tagid):
        # r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token={self.token}&tagid={tagid}")
        self.params["tagid"] = tagid
        data = openfile()
        return self.send(data["gettagusers"])

    # 删除标签成员接口
    def test_deletetagusers(self, tagid, userlist, partylist=None):
        # access_token = get_token()
        if partylist is None:
            partylist = "1"
        # body = {
        #     "tagid": tagid,
        #     "userlist": userlist,
        #     "partylist": partylist
        # }
        # r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/tag/deltagusers?access_token={self.token}", json=body)
        self.params["tagid"] = tagid
        self.params["userlist"] = userlist
        self.params["partylist"] = partylist
        data = openfile()
        return self.send(data["deletetagusers"])
