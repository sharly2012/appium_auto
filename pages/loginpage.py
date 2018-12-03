#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author: sharly

from utils.basepage import BasePage
from appium.webdriver.common.mobileby import By


class LoginPage(BasePage):
    login_image = (By.ID, "com.elab.dmbrand:id/riv_avatar")
    texts = "com.elab.dmbrand:id/tv_text"
    message_notice = (By.XPATH, "//*[@text='消息通知'")
    house_type_collect = (By.XPATH, "//*[@text='户型收藏'")
    recommend = (By.XPATH, "//*[@text='成功推荐'")
    visit_history = (By.XPATH, "//*[@text='浏览历史'")
    person_setting = (By.XPATH, "//*[@text='个人设置'")
    login_immediately = [(281, 1199), (799, 1326)]
    login_mobile = (By.ID, "com.elab.dmbrand:id/txt_login_no")
    verify_code = (By.ID, "com.elab.dmbrand:id/txt_login_pwd")
    login_button = (By.ID, "com.elab.dmbrand:id/tv_enter_up")

