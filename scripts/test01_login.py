import unittest

from parameterized import parameterized

import api
from api.api_login import ApiLogin
from tools.assert_common import assert_common
from tools.get_log import GetLog
from tools.read_yaml import read_yaml
log = GetLog.get_logger()

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.login = ApiLogin()

    @parameterized.expand(read_yaml("login.yaml"))
    def test_login(self, mobile, password):
        result = self.login.api_login(mobile, password)
        print("登陆结果：", result.json())
        log.info("登陆的结果为：",result.json())
        r = result.json()
        # 断言
        assert_common(self, result)
        # 提取token
        token = r.get("data")
        # 追加到公共变量head
        api.head["Authorization"] = "Bearer " + token
        print("追加后的head为： ", api.head)
        log.info("追加后的api.head为：",api.head)
