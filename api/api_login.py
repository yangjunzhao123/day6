import api
import requests

from tools.get_log import GetLog

log = GetLog().get_logger()
class ApiLogin:
    def __init__(self):
        self.url_login = api.host + "/api/sys/login"
        log.info("登陆的url为：",self.url_login)

    def api_login(self,mobile,password):
        data = {"mobile":mobile,"password":password}
        log.info("请求的head：",api.head)
        return requests.post(url=self.url_login,json=data,headers=api.head)
