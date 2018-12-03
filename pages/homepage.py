#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author: sharly

from utils.basepage import BasePage
from appium.webdriver.common.mobileby import By


class HomePage(BasePage):
    login_icon = [(86, 107), (115, 115)]
    login_icon01 = (By.ID, "com.elab.dmbrand:id/iv_login")
    update_cancel = (By.ID, "com.elab.dmbrand:id/tv_cancel")
    update_update = (By.ID, "com.elab.dmbrand:id/tv_update")
    read_more = (By.ID, "com.elab.dmbrand:id/iv_read_more")
    news_title = (By.ID, "com.elab.dmbrand:id/tv_title")
    news_description = (By.ID, "com.elab.dmbrand:id/tv_desc")
