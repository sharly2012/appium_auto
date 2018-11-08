#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author: sharly


from utils.logger import Logger
from utils.tools import Device
from utils.shell import Shell

logger = Logger(logger="environment").get_log()


class Environment(object):
    def __init__(self):
        self.devices = Device.get_android_devices()
        self.appium_v = Shell.invoke('appium -v').splitlines()[0].strip()
        self.check_appium()
        self.check_devices()

    def check_appium(self):
        logger.info('检查环境...')
        """检查appium版本"""
        if not self.appium_v:
            logger.error('appium 版本有问题')
            exit()
        else:
            logger.info('appium version {}'.format(self.appium_v))

    def check_devices(self):
        """检查设备"""
        if not self.devices:
            logger.error('没有设备连接')
            exit()
        else:
            logger.info('已连接设备:', self.devices)


if __name__ == '__main__':
    env = Environment()
    env.check_appium()
    env.check_devices()
