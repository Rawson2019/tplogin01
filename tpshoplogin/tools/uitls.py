"""
全局工具类
"""
from selenium import webdriver


class DriverUtil(object):
    """浏览器驱动类"""

    _driver = None

    @classmethod
    def get_driver(cls):
        """获取浏览器驱动方法"""
        if cls._driver is None:
            cls._driver = webdriver.Chrome()
            cls._driver.get('http://localhost/index.php/')
            cls._driver.maximize_window()
            cls._driver.implicitly_wait(15)
        return cls._driver

    @classmethod
    def quit_driver(cls):
        """退出浏览器驱动方法"""
        if cls._driver:
            cls._driver.quit()
            cls._driver = None
