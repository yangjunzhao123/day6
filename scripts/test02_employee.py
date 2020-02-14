import unittest

from parameterized import parameterized

import api
from api.api_employee import ApiEmployee

from tools.assert_common import assert_common
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()
class TestEmployee(unittest.TestCase):
    # 1.初始化方法
    @classmethod
    def setUpClass(cls):
        # 获取apiemployee对象
        cls.api = ApiEmployee()

    # 2.新增员工 接口测试方法
    @parameterized.expand(read_yaml("employee_login.yaml"))
    def test01_post(self, username, mobile, worNumber):
        # 调用新增接口
        r = self.api.api_post_employee(username, mobile, worNumber)
        # 断言
        assert_common(self, r)
        print("新增员工结果：", r.json())
        # 提取user_id
        api.user_id = r.json().get("data").get("id")
        log.info("员工的id：",api.user_id)
        print("员工user_id值为：", api.user_id)

    def test02_put(self):
        #参数准备
        data = {"username":"ya-g-11"}
        # 调用修改员工接口
        r = self.api.api_put_employee(data.get("username"))
        log.info("修改员工的：", r)


    def test03_get(self):
        r = self.api.api_get_employee()

    def test04_delete(self):
        # 调用删除员工接口
        r = self.api.api_delete_employee()
        print("删除结果为：", r.json())
        # 断言
        assert_common(self, r)
