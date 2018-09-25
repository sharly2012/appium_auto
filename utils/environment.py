#!/usr/bin/python3
# -*- coding: utf-8 -*-

import yaml
from utils.config import Config
from utils.log import Log
from utils.tools import Device
from utils.shell import Shell
from utils.shell import ADB


class EnvironmentInfo(yaml.YAMLObject):
    yaml_loader = yaml.SafeLoader
    yaml_tag = '!EnvironmentInfo'

    def __init__(self, appium, devices, apk, pages_yaml, xml_report, html_report, app_activity, app_package):
        self.appium = appium
        self.pages_yaml = pages_yaml
        self.xml_report = xml_report
        self.html_report = html_report
        self.apk = apk
        self.devices = devices
        self.app_activity = app_activity
        self.app_package = app_package


class DeviceInfo(yaml.YAMLObject):
    yaml_loader = yaml.SafeLoader
    yaml_tag = '!DeviceInfo'

    def __init__(self, device_name, platform_name, platform_version):
        self.device_name = device_name
        self.platform_name = platform_name
        self.platform_version = platform_version


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@singleton
class Environment:
    def __init__(self):
        self.devices = Device.get_android_devices()
        self.appium_v = Shell.invoke('appium -v').splitlines()[0].strip()
        self.config = Config()
        self.check_environment()
        self.save_environment()

    def check_environment(self):
        Log.i('检查环境...')
        # 检查appium版本
        if not self.appium_v:
            Log.e('appium 版本有问题')
            exit()
        else:
            Log.i('appium version {}'.format(self.appium_v))
        # 检查设备
        if not self.devices:
            Log.e('没有设备连接')
            exit()
        else:
            Log.i('已连接设备:', self.devices)

    def save_environment(self):
        infos = []
        env_path = self.config.env_yaml_path
        apk_path = self.config.apk_path
        pages_yaml_path = self.config.pages_yaml_path
        xml_report_path = self.config.xml_report_path
        html_report_path = self.config.html_report_path
        app_activity = self.config.app_activity
        app_package = self.config.app_package
        for deviceName in self.devices:
            info = DeviceInfo(deviceName, "Android", ADB(deviceName).get_android_version())
            infos.append(info)
        env_info = EnvironmentInfo(self.appium_v, infos, apk_path, pages_yaml_path, xml_report_path, html_report_path,
                                   app_activity, app_package)
        with open(env_path, 'w') as f:
            yaml.dump(env_info, f, default_flow_style=False)
            Log.i('保存环境配置 Path:' + env_path)

    def get_environment_info(self) -> EnvironmentInfo:
        env_path = self.config.env_yaml_path
        with open(env_path, 'r') as f:
            env_info = yaml.safe_load(f)
        return env_info

    def get_inited_config(self):
        return self.config


if __name__ == '__main__':
    env = Environment()
    env.check_environment()
    env.save_environment()
    info = env.get_environment_info()
    print(info.app_package)
