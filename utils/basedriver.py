#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author: sharly

import time
from appium import webdriver
from utils.baseutil import BaseUtil


class BaseDriver:
    def __init__(self):
        self.platformName = BaseUtil().get_yaml_value("EnvironmentInfo", "platformName")
        self.platformVersion = BaseUtil().get_yaml_value("EnvironmentInfo", "platformVersion")
        self.deviceName = BaseUtil().get_yaml_value("EnvironmentInfo", "deviceName")
        self.browserName = BaseUtil().get_yaml_value("EnvironmentInfo", "browserName")
        self.apk = BaseUtil().get_yaml_value("EnvironmentInfo", "apk")
        self.appPackage = BaseUtil().get_yaml_value("EnvironmentInfo", "appPackage")
        self.appActivity = BaseUtil().get_yaml_value("EnvironmentInfo", "appActivity")
        self.automationName = BaseUtil().get_yaml_value("EnvironmentInfo", "automationName")
        self.unicodeKeyboard = BaseUtil().get_yaml_value("EnvironmentInfo", "unicodeKeyboard")
        self.resetKeyboard = BaseUtil().get_yaml_value("EnvironmentInfo", "resetKeyboard")
        self.newCommandTimeout = BaseUtil().get_yaml_value("EnvironmentInfo", "newCommandTimeout")
        self.noReset = BaseUtil().get_yaml_value("EnvironmentInfo", "noReset")
        self.chromeOptions = BaseUtil().get_yaml_value("EnvironmentInfo", "chromeOptions")

    def applet_driver(self):
        desired_caps = {
            'platformName': self.platformName,
            'platformVersion': self.platformVersion,
            'deviceName': self.deviceName,
            'appPackage': self.appPackage,
            'appActivity': self.appActivity,
            'noReset': self.noReset,
            'chromeOptions': self.chromeOptions

        }

        applet_drive = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(5)
        return applet_drive

    def app_driver(self):
        desired_caps = {
            'platformName': self.platformName,
            'platformVersion': self.platformVersion,
            'deviceName': self.deviceName,
            'appPackage': self.appPackage,
            'appActivity': self.appActivity,
            'noReset': self.noReset
        }

        app_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(6)
        return app_driver


if __name__ == '__main__':
    apk = BaseDriver().apk
    print(apk)
