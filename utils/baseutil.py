#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author: sharly

import configparser
import yaml
from utils.logger import Logger

logger = Logger(logger="BaseUtil").get_log()


class BaseUtil:
    def __init__(self):
        self.root_path = 'E:/PycharmProjects/appium_auto'

    def get_config_value(self, section, key):
        """get the section value in the config file"""
        config_path = self.root_path + "/config/config.ini"
        config = configparser.ConfigParser()
        config.read(config_path)
        value = config.get(section, key)
        logger.info("The value of %s is %s" % (key, value))
        return value

    def get_yaml_value(self, option, key):
        """get the option value in the yaml file"""
        yaml_path = self.root_path + "/config/environment.yaml"
        with open(yaml_path, 'r') as f:
            temp = yaml.load(f.read())
        value = temp[option][key]
        logger.info("The value of %s is %s" % (key, value))
        return value

    def set_root_path(self, path):
        """set the root path"""
        self.root_path = path
        logger.info("Current root path is %s" % self.root_path)

    def get_root_path(self):
        """get the root path"""
        return self.root_path
        logger.info("Current root path is %s" % self.root_path)
