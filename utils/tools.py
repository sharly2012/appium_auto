#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author: sharly

from utils.shell import Shell
from utils.logger import Logger

logger = Logger(logger="tools").get_log()


class Device:
    @staticmethod
    def get_android_devices():
        android_devices_list = []
        for device in Shell.invoke('adb devices').splitlines():
            if 'device' in device and 'devices' not in device:
                device = device.split('\t')[0]
                android_devices_list.append(device)
        return android_devices_list


if __name__ == '__main__':
    devices = Device.get_android_devices()
    logger.info("devices: % s" % devices)
