#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author: sharly

import pytest
import allure
from utils.basedriver import BaseDriver
from utils.logger import Logger
from pages.homepage import HomePage
from pages.loginpage import LoginPage
from pages.personsetting import PersonSetting

logger = Logger(logger="TestLogin").get_log()


@allure.feature("Login Test")
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

    @allure.severity(pytest.allure.severity_level.NORMAL)
    @allure.story("login success")
    @allure.testcase("Login test pass")
    def test_login(self):
        homepage = HomePage(self.driver)
        homepage.click(homepage.update_cancel)
        homepage.tap(homepage.login_icon)
        login_page = LoginPage(self.driver)
        login_page.click(login_page.login_image)
        login_page.tap(login_page.login_immediately)
        login_page.clear_input(login_page.login_mobile)
        login_page.input_text(login_page.login_mobile, "15601791033")
        login_page.clear_input(login_page.verify_code)
        login_page.input_text(login_page.verify_code, "150723")
        login_page.click(login_page.login_button)
        personsetting = PersonSetting(self.driver)
        # mobile = personsetting.get_element_text(personsetting.mobile)
        # assert mobile == "15601791033"

        logger.info("Login success")

    @allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.story("login success")
    @allure.testcase("Login test fail")
    def test_login002(self):
        pass

    @allure.severity(pytest.allure.severity_level.MINOR)
    @allure.story("login fail")
    @allure.testcase("Login test 003")
    def test_login003(self):
        pass

    @allure.severity(pytest.allure.severity_level.NORMAL)
    @allure.story("login fail")
    @allure.testcase("Login test 004")
    def test_login004(self):
        pass


if __name__ == '__main__':
    pytest.main(["-s", "test_login.py"])
