#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author: sharly

from utils.basepage import BasePage
from appium.webdriver.common.mobileby import By


class PersonSetting(BasePage):
    head_icon = (By.ID, "com.elab.dmbrand:id/siv_avatar")
    short_name = (By.ID, "com.elab.dmbrand:id/siv_nickname")
    mobile = (By.ID, "com.elab.dmbrand:id/siv_mobile")
    sex_setting = (By.ID, "com.elab.dmbrand:id/siv_gender")
    city_setting = (By.ID, "com.elab.dmbrand:id/siv_city")
    system_setting = (By.ID, "com.elab.dmbrand:id/siv_system_setting")
