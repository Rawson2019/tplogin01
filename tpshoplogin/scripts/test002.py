import allure
import pytest


class Test002():
    @allure.step(title="正在执行登录操作")
    def test001(self):
        print("zhixinglema?")

    @allure.step(title="正在执行数据传输")
    def test002(self):
        print("zhixinglema?")

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    def test003(self):
        allure.attach("描述","正在打印test003")
        print("zhixinglema?")

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test004(self):
        # allure.attach("描述",f.read(),allure.attach_type.PNG)
        # PNG必须大写
        with open("./image/fail.png","rb") as f:
            allure.attach("描述",f.read(),allure.attach_type.PNG)
            print("zhixinglema?")