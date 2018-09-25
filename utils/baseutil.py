#!/usr/bin/python3
# -*- coding: utf-8 -*-
import configparser
import yaml


class BaseUtil:
    def __init__(self):
        self.root_path = 'D:/PycharmProjects/appium_auto'

    def get_config_value(self, section, key):
        config_path = self.root_path + "/conf/config.ini"
        config = configparser.ConfigParser()
        config.read(config_path)
        value = config.get(section, key)
        return value

    def get_yaml_value(self, option, key):
        yaml_path = self.root_path + "/config/environment.yaml"
        with open(yaml_path, 'r') as f:
            temp = yaml.load(f.read())
        value = temp[option][key]
        return value

    def set_root_path(self, path):
        self.root_path = path

    def get_root_path(self):
        return self.root_path
