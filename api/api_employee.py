import api
import requests

from tools.get_log import GetLog

log = GetLog.get_logger()
class ApiEmployee():
    # 初始化
    def __init__(self):
        # 新增员工
        self.url_post = api.host + "/api/sys/user"
        # 修改，查询，删除员工
        self.url_xcs = api.host + "/api/sys/user/{}"
        # log.info("添加员工的url为：",self.url_post)
        # log.info("修改，查询和删除公用方法：", self.url_xcs)
    # 新增员工
    def api_post_employee(self,username,mobile,workNumbe):
        # 1.参数数据
        data = {"username": username,"mobile": mobile,"workNumber": workNumbe}
        # 2.调用post方法》返回相应对象
        log.info("添加员工的数据data为：{},添加员工返回的id为：{}".format(data,api.head))
        return requests.post(url=self.url_post,json=data,headers=api.head)

    # 修改员工
    def api_put_employee(self,username):
        # 参数数据
        data = {"username": username}
        # 2.调用put方法》返回相应对象
        log.info("修改员工的数据data为：{},修改员工返回的id为：{}".format(data, api.head))
        return requests.put(url=self.url_xcs.format(api.user_id),json=data,headers=api.head)
    # 查询员工
    def api_get_employee(self):
        # 1.调用get方法》返回相应对象
        log.info("查询员工返回的id为：{}".format(api.head))
        return requests.get(url=self.url_xcs.format(api.user_id),headers=api.head)

    # 删除员工
    def api_delete_employee(self):
        # 1.调用delete方法》返回相应对象
        log.info("删除员工返回的id为：{}".format(api.head))
        return requests.delete(url=self.url_xcs.format(api.user_id),headers=api.head)