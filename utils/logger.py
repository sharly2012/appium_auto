#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author: sharly

import time
import logging


class Logger(object):
    """Saves the log to the specified path file and Specifies the level"""

    def __init__(self, logger):
        """create logger files"""
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        """create handle to write the log"""
        now = time.strftime("%Y-%m-%d_%H_%M_%S")
        log_path = "E:/PycharmProjects/appium_auto/logs/"
        log_name = log_path + now + '.log'

        file_handle = logging.FileHandler(log_name, encoding="utf-8")
        file_handle.setLevel(logging.INFO)

        """create a handle to output the log to console"""
        control_handle = logging.StreamHandler()
        control_handle.setLevel(logging.INFO)

        # exchange the handle
        formatter = logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s')
        file_handle.setFormatter(formatter)
        control_handle.setFormatter(formatter)

        """add handle to log"""
        self.logger.addHandler(file_handle)
        self.logger.addHandler(control_handle)

    def get_log(self):
        return self.logger
