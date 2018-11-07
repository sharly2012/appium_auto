#!/usr/bin/python3
# -*- coding: utf-8 -*-
from utils.baseutil import BaseUtil
from utils.logger import Logger

logger = Logger(logger="Config").get_log()


class Config:

    def __init__(self):
        self.apk_name = BaseUtil().get_config_value("apk_info", "apk_name")
        self.apk_path = BaseUtil().root_path + "/apk/" + self.apk_name + ".apk"
        self.xml_report_path = BaseUtil().root_path + "/report/xml"
        self.html_report_path = BaseUtil().root_path + "/report/html"
        self.env_yaml_path = BaseUtil().root_path + "/config/environment.yaml"
        self.app_activity = BaseUtil().get_config_value("apk_info", "app_activity")
        self.app_package = BaseUtil().get_config_value("apk_info", "app_package")
        self.account = BaseUtil().get_config_value("account_info", "account")
        self.password = BaseUtil().get_config_value("account_info", "password")


if __name__ == '__main__':
    conf = Config()
    logger.info(conf.apk_name)
    logger.info(conf.apk_path)
    logger.info(conf.xml_report_path)
    logger.info(conf.html_report_path)
    logger.info(conf.env_yaml_path)
    logger.info(conf.app_activity)
    logger.info(conf.app_package)
    logger.info(conf.account)
    logger.info(conf.password)
