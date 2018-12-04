#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author: sharly

import time
from appium import webdriver
from utils.environment import Environment
from utils.baseutil import BaseUtil
from utils.logger import Logger

logger = Logger(logger="BaseDriver").get_log()


class BaseDriver:
    def __init__(self):
        self.env = Environment()
        self.platformName = BaseUtil().get_yaml_value("EnvironmentInfo", "platformName")
        self.platformVersion = BaseUtil().get_yaml_value("EnvironmentInfo", "platformVersion")
        self.deviceName = BaseUtil().get_yaml_value("EnvironmentInfo", "deviceName")
        self.browserName = BaseUtil().get_yaml_value("EnvironmentInfo", "browserName")
        self.app = BaseUtil().get_yaml_value("EnvironmentInfo", "app")
        self.appPackage = BaseUtil().get_yaml_value("EnvironmentInfo", "appPackage")
        self.appActivity = BaseUtil().get_yaml_value("EnvironmentInfo", "appActivity")
        self.automationName = BaseUtil().get_yaml_value("EnvironmentInfo", "automationName")
        self.unicodeKeyboard = BaseUtil().get_yaml_value("EnvironmentInfo", "unicodeKeyboard")
        self.resetKeyboard = BaseUtil().get_yaml_value("EnvironmentInfo", "resetKeyboard")
        self.newCommandTimeout = BaseUtil().get_yaml_value("EnvironmentInfo", "newCommandTimeout")
        self.noReset = BaseUtil().get_yaml_value("EnvironmentInfo", "noReset")
        self.chromeOptions = BaseUtil().get_yaml_value("EnvironmentInfo", "chromeOptions")

    def applet_driver(self):
        try:
            desired_caps = {
                'platformName': self.platformName,
                'deviceName': self.deviceName,
                'appPackage': self.appPackage,
                'appActivity': self.appActivity,
                'noReset': self.noReset,
                'chromeOptions': self.chromeOptions

            }

            applet_drive = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
            time.sleep(5)
            return applet_drive
        except Exception as e:
            logger.info("Can't open the WeChat applet driver")
            logger.error(e)

    def app_driver(self):
        try:
            desired_caps = {
                'platformName': self.platformName,
                'deviceName': self.deviceName,
                'appPackage': self.appPackage,
                'appActivity': self.appActivity,
                'noReset': self.noReset
            }

            app_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
            time.sleep(6)
            return app_driver
        except Exception as e:
            logger.info("Can't open the app driver")
            logger.error(e)


if __name__ == '__main__':
    apk = BaseDriver().app_driver()
