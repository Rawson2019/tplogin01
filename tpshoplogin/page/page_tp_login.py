import page
from base.base import Base

class PageTpLogin(Base):

    # 点击登录链接
    def page_index_login(self):
        self.base_login_click(page.index_login_btn)
    # 登录页用户名输入
    def page_login_name_input(self,username):
        self.base_login_input(page.login_name_input,username)

    # 登录页密码输入
    def page_login_pwd_input(self,pwd):
        self.base_login_input(page.login_pwd_input,pwd)
    # 登录验证码输入
    def page_login_verify_input(self,verify):
        self.base_login_input(page.login_verify_input,verify)
    # 登陆按钮
    def page_lonin_login_btn(self):
        self.base_login_click(page.login_login_btn)
    def page_login_all(self,username,pwd,verify):
        # self.page_index_login()
        self.page_login_name_input(username)
        self.page_login_pwd_input(pwd)
        self.page_login_verify_input(verify)
        self.page_lonin_login_btn()