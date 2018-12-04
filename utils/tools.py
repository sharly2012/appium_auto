#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author: sharly

import os
from utils.shell import Shell
from utils.logger import Logger

logger = Logger(logger="tools").get_log()


class AndroidEnvironment(object):
    """check the android environment"""
    if "ANDROID_HOME" in os.environ:
        command = os.path.join(
            os.environ["ANDROID_HOME"],
            "platform-tools",
            "adb")
    else:
        raise EnvironmentError(
            "Adb not found in $ANDROID_HOME path: %s." %
            os.environ["ANDROID_HOME"])


class ADB(object):
    """
      args:  device_id
    """

    def __init__(self, device_id=""):

        if device_id == "":
            self.device_id = ""
        else:
            self.device_id = "-s %s" % device_id

    def adb(self, args):
        cmd = "%s %s %s" % (AndroidEnvironment().command, self.device_id, str(args))
        return Shell.invoke(cmd)

    def shell(self, args):
        cmd = "%s %s shell %s" % (AndroidEnvironment().command, self.device_id, str(args),)
        return Shell.invoke(cmd)

    def get_device_state(self):
        """get the device status： offline | bootloader | device"""
        return self.adb("get-state").stdout.read().strip()

    def get_device_id(self):
        """ get device id，return serialNo"""
        return self.adb("get-serialno").stdout.read().strip()

    def get_android_version(self):
        """get android version"""
        return self.shell(
            "getprop ro.build.version.release").strip()

    def get_sdk_version(self):
        """get the sdk version"""
        return self.shell("getprop ro.build.version.sdk").strip()

    @staticmethod
    def get_android_devices():
        """get the android devices"""
        android_devices_list = []
        for device in Shell.invoke('adb devices').splitlines():
            if 'device' in device and 'devices' not in device:
                device = device.split('\t')[0]
                android_devices_list.append(device)
        return android_devices_list


if __name__ == '__main__':
    devices = ADB().get_android_devices()
    print(devices)
