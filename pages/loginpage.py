#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from utils.basepage import BasePage


class LoginPage(BasePage):
    login_image = "id>=com.elab.dmbrand:id/riv_avatar"
    texts = "ids=>com.elab.dmbrand: id / tv_text"
    message_notice = "xpath>=//*[@text='消息通知']"
    house_type_collect = "xpath>=//*[@text='户型收藏']"
    recommend = "xpath>=//*[@text='成功推荐']"
    visit_history = "xpath>=//*[@text='浏览历史']"
    person_setting = "xpath>=//*[@text='个人设置']"
    login_immediately = [(281, 1199), (799, 1326)]
