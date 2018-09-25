#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
import logging
from utils.baseutil import BaseUtil


class Log:
    @staticmethod
    def e(msg, list_msg=[]):
        if list_msg:
            Log.show_list(msg, list_msg, Log.e)
        else:
            ColorLog.show_error(get_now_time() + " [Error]:" + "".join(msg))

    @staticmethod
    def w(msg, list_msg=[]):
        if list_msg:
            Log.show_list(msg, list_msg, Log.w)
        else:
            ColorLog.show_warn(get_now_time() + " [Warn]:" + "".join(msg))

    @staticmethod
    def i(msg, list_msg=[]):
        if list_msg:
            Log.show_list(msg, list_msg, Log.i)
        else:
            ColorLog.show_info(get_now_time() + " [Info]:" + "".join(msg))

    @staticmethod
    def d(msg, list_msg=[]):
        if list_msg:
            Log.show_list(msg, list_msg, Log.d)
        else:
            ColorLog.show_debug(get_now_time() + " [Debug]:" + "".join(msg))

    @staticmethod
    def show_list(msg, list_msg, f):
        temp = msg + "[ " + "\t".join(list_msg) + " ]"
        f(temp)


class ColorLog:
    @staticmethod
    def c(msg, colour):
        try:
            from termcolor import colored, cprint
            p = lambda x: cprint(x, '%s' % colour)
            return p(msg)
        except:
            print(msg)

    @staticmethod
    def show_verbose(msg):
        ColorLog.c(msg, 'white')

    @staticmethod
    def show_debug(msg):
        ColorLog.c(msg, 'blue')

    @staticmethod
    def show_info(msg):
        ColorLog.c(msg, 'green')

    @staticmethod
    def show_warn(msg):
        ColorLog.c(msg, 'yellow')

    @staticmethod
    def show_error(msg):
        ColorLog.c(msg, 'red')


def get_now_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))


class Logger(object):
    def __init__(self, logger):
        """
        将日志保存到指定的路径文件中
        指定日志的级别，以及调用文件
        """

        # 创建logger文件
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handle，用来写入日志文件
        now = time.strftime("%Y-%m-%d_%H_%M_%S")
        # log_path = os.path.dirname(os.path.abspath('.')) + '/logs/'
        log_path = BaseUtil().get_root_path() + '/logs/'
        log_name = log_path + now + '.log'

        file_handle = logging.FileHandler(log_name, encoding="utf-8")
        file_handle.setLevel(logging.INFO)

        # 创建一个handle，用来输入日志到控制台
        control_handle = logging.StreamHandler()
        control_handle.setLevel(logging.INFO)

        # 将输出的hangdle格式进行转换
        formatter = logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s')
        file_handle.setFormatter(formatter)
        control_handle.setFormatter(formatter)

        # 给logger添加handle
        self.logger.addHandler(file_handle)
        self.logger.addHandler(control_handle)

    def get_log(self):
        return self.logger
