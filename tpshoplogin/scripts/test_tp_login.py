import pytest
import os
import sys
sys.path.append(os.getcwd())

from page.page_tp_login import PageTpLogin
from tools.uitls import DriverUtil

def get_data():
    return [("13920964528","123456","8888")]
class TestTpLogin(object):
    # 初始化
    def setup(self):
        self.driver = DriverUtil().get_driver()
        self.login = PageTpLogin(self.driver)

    # 结束
    def teardown(self):
        self.login.driver.quit()


    # 测试用
    @pytest.mark.parametrize("username,pwd,verify",get_data())
    def test_login(self,username,pwd,verify):
        self.login.page_login_all(username,pwd,verify)