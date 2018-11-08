#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author: sharly

import os
import subprocess


class Shell:
    @staticmethod
    def invoke(cmd):
        """通过shell来执行"""
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        o = output.decode("utf-8")
        return o


# 检查ANDROID环境变量
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
        cmd = "%s %s %s" % (command, self.device_id, str(args))
        return Shell.invoke(cmd)

    def shell(self, args):
        cmd = "%s %s shell %s" % (command, self.device_id, str(args),)
        return Shell.invoke(cmd)

    def get_device_state(self):
        """
        获取设备状态： offline | bootloader | device
        """
        return self.adb("get-state").stdout.read().strip()

    def get_device_id(self):
        """
        获取设备id号，return serialNo
        """
        return self.adb("get-serialno").stdout.read().strip()

    def get_android_version(self):
        """
        获取设备中的Android版本号
        """
        return self.shell(
            "getprop ro.build.version.release").strip()

    def get_sdk_version(self):
        """
        获取设备SDK版本号
        """
        return self.shell("getprop ro.build.version.sdk").strip()
