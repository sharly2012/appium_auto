#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author: sharly


from utils.logger import Logger
from utils.tools import ADB
from utils.shell import Shell

logger = Logger(logger="environment").get_log()


class Environment(object):
    def __init__(self):
        self.devices = ADB().get_android_devices()
        self.appium_version = Shell.invoke('appium -v').splitlines()[0].strip()
        self.check_appium()
        self.check_devices()

    def check_appium(self):
        """check appium version"""
        logger.info('Start check appium version...')
        if not self.appium_version:
            logger.error('Appium error, please check')
            exit()
        else:
            logger.info("Appium version: %s" % self.appium_version)

    def check_devices(self):
        """check devices"""
        logger.info("Start check devices...")
        if not self.devices:
            logger.error('Not have any devices connected')
            exit()
        else:
            for device in self.devices:
                logger.info('Connect device: %s' % device)


if __name__ == '__main__':
    Environment()
