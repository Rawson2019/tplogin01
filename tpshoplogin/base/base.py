from selenium.webdriver.support.wait import WebDriverWait

from tools.uitls import DriverUtil


class Base(object):
    # 初始化
    def __init__(self,driver):
        self.driver = driver
        # self.driver=driver
    # 元素定位
    def base_find_element(self,loc,timeout=30,poll=0.5):
        # 返回元素值
       return WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll).until(lambda x:x.find_element(*loc))

    # 输入方法
    def base_login_input(self,loc,value):
        el = self.base_find_element(loc)
        el.clear()
        el.send_keys(value)


    # 输入方法
    def base_login_click(self,loc):
        self.base_find_element(loc).click()
    # 获取文本信息
    def base_get_text(self,loc):
        return self.base_find_element(loc).text
    # 获取截图
    def base_get_img(self):
        self.driver.get_screenshot_as_file("./image/fail.png")
