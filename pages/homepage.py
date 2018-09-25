from utils.action import ElementActions
from appium.webdriver.common.mobileby import By


class HomePage(ElementActions):
    login_text = (By.ID, 'com.czbix.v2ex:id/username_tv')
    account = (By.ID, 'com.czbix.v2ex:id/account')
    password = (By.ID, 'com.czbix.v2ex:id/password')
