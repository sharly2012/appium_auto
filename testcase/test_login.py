#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author: sharly

import pytest
import allure
from utils.basedriver import BaseDriver
from utils.logger import Logger
from pages.homepage import HomePage
from pages.loginpage import LoginPage

logger = Logger(logger="TestLogin").get_log()


@allure.feature("首页")
class TestLogin:

    @classmethod
    def setup_class(cls):
        base_driver = BaseDriver()
        cls.driver = base_driver.app_driver()

    @classmethod
    def teardown_class(cls):
        cls.driver.close_app()

    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    @allure.feature("Home Page")
    @allure.story("login")
    def test_login(self):
        homepage = HomePage(self.driver)
        homepage.tap(homepage.login_icon)
        login_page = LoginPage(self.driver)
        login_page.click(login_page.login_image)
        login_page.tap(login_page.login_immediately)

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.story("test")
    def test_login2(self):
        pass

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    @allure.story("test")
    def test_login3(self):
        pass

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    @allure.story("test")
    def test_login4(self):
        pass


if __name__ == '__main__':
    pytest.main(["-s", "test_login.py"])
