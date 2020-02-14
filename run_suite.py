# 1.导包
import os
import unittest

from config import base_url
from tools.HTMLTestRunner import HTMLTestRunner
# 2.定义测试套件


suite = unittest.defaultTestLoader.discover(base_url + os.sep+"scripts",pattern="test*.py")
with open(base_url+os.sep + "report"+ os.sep + "report.html","wb")as f:
    HTMLTestRunner(stream=f).run(suite)