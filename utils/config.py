#!/usr/bin/python3
# -*- coding: utf-8 -*-

import configparser
from utils.log import Log
from utils.baseutil import BaseUtil


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


class Config:
    DEFAULT_CONFIG_DIR = BaseUtil().get_root_path() + "/config/config.ini"
    BASE_PATH_DIR = BaseUtil().get_root_path()

    # titles:
    TITLE_NAME = "name"
    TITLE_ACCOUNT = "account"
    # values:
    # [name]
    VALUE_APP = "apk"
    VALUE_APP_ACTIVITY = "app_activity"
    VALUE_APP_PACKAGE = "app_package"
    # [account]
    VALUE_ACCOUNT = "account"
    VALUE_PASSWORD = "password"

    def __init__(self):
        self.path = Config.DEFAULT_CONFIG_DIR
        self.cp = configparser.ConfigParser()
        self.cp.read(self.path)
        Log.i('Init config...config path: ' + self.path)
        apk_name = self.get_config(Config.TITLE_NAME, Config.VALUE_APP)
        self.apk_path = Config.BASE_PATH_DIR + '/apk/' + apk_name
        self.xml_report_path = Config.BASE_PATH_DIR + '/report/xml'
        self.html_report_path = Config.BASE_PATH_DIR + '/report/html'
        self.pages_yaml_path = Config.BASE_PATH_DIR + '/pages/yaml'
        self.env_yaml_path = Config.BASE_PATH_DIR + '/config/environment.yaml'
        self.app_activity = self.get_config(Config.TITLE_NAME, Config.VALUE_APP_ACTIVITY)
        self.app_package = self.get_config(Config.TITLE_NAME, Config.VALUE_APP_PACKAGE)
        self.account = self.get_config(Config.TITLE_ACCOUNT, Config.VALUE_ACCOUNT)
        self.password = self.get_config(Config.TITLE_ACCOUNT, Config.VALUE_PASSWORD)

    def set_config(self, title, value, text):
        self.cp.set(title, value, text)
        with open(self.path, "w+") as f:
            return self.cp.write(f)

    def add_config(self, title):
        self.cp.add_section(title)
        with open(self.path, "w+") as f:
            return self.cp.write(f)

    def get_config(self, title, value):
        return self.cp.get(title, value)
