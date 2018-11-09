#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author: sharly

import inspect
import time
import allure
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *
from utils.logger import Logger
from utils.baseutil import BaseUtil

logger = Logger(logger='BasePage').get_log()


class BasePage(object):

    def __init__(self, driver):
        """初始化方法"""
        self.driver = driver
        self.width = self.driver.get_window_size()['width']
        self.height = self.driver.get_window_size()['height']
        self.timeout_time = 15
        self.wait_time = 2

    def reset(self):
        """重置一下driver"""
        logger.info("reset the driver...")
        self.width = self.driver.get_window_size()['width']
        self.height = self.driver.get_window_size()['height']
        return self

    def find_element(self, *locator):
        """查找元素"""
        try:
            # 元素可见时，返回查找到的元素；以下入参为元组的元素，需要加*
            WebDriverWait(self.driver, 30, 0.5).until(lambda driver: driver.find_element(*locator).is_displayed())
            return self.driver.find_element(*locator)
        except NoSuchElementException:
            logger.warning('Can not find element: %s' % locator[1])
            raise
        except TimeoutException:
            logger.warning('Can not find element: %s' % locator[1])

    def find_elements(self, by, value):
        """定位一组元素"""
        try:
            if by == "id":
                WebDriverWait(self.driver, self.timeout_time).until(
                    lambda driver: driver.find_element_by_id(value).is_displayed())
                self.driver.implicitly_wait(self.wait_time)
                elements = self.driver.find_element_by_id(value)
                return elements
            if by == "name":
                find_name = "//*[@text='%s']" % value
                WebDriverWait(self.driver, self.timeout_time).until(
                    lambda driver: driver.find_element_by_xpath(find_name).is_displayed())
                self.driver.implicitly_wait(self.wait_time)
                elements = self.driver.find_element_by_xpath(find_name)
                return elements
            if by == "xpath":
                WebDriverWait(self.driver, self.timeout_time).until(
                    lambda driver: driver.find_element_by_xpath(value).is_displayed())
                self.driver.implicitly_wait(self.wait_time)
                elements = self.driver.find_element_by_xpath(value)
                return elements
            if by == "class_name":
                WebDriverWait(self.driver, self.timeout_time).until(
                    lambda driver: driver.find_element_by_class_name(value).is_displayed())
                self.driver.implicitly_wait(self.wait_time)
                elements = self.driver.find_element_by_class_name(value)
                return elements
            if by == "content":
                WebDriverWait(self.driver, self.timeout_time).until(
                    lambda driver: driver.find_element_by_accessibility_id(value).is_displayed())
                self.driver.implicitly_wait(self.wait_time)
                elements = self.driver.find_element_by_accessibility_id(value)
                return elements
            else:
                raise NameError("Please Enter correct elements value")
        except NoSuchElementException:
            logger.warning("Can not find elements: %s" % value)
            raise

    def click(self, locator):
        """封装点击"""
        logger.info('Click element by %s: %s...' % (locator[0], locator[1]))
        try:
            self.find_element(*locator).click()
        except AttributeError as e:
            logger.warning("无法点击元素: %s" % e)

    def clear_input(self, locator):
        """输入文本框清空操作"""
        element = self.find_element(*locator)
        try:
            element.clear()
            logger.info('Clear input-box: %s...' % locator[1])
        except NameError as ne:
            logger.warning("Failed to clear in input box with %s" % ne)
            self.get_screent_img()

    def input_text(self, locator, text):
        """在文本框输入文本"""
        self.find_element(*locator).clear()
        logger.info('Input element by %s: %s...' % (locator[0], locator[1]))
        logger.info('Input: %s' % text)
        try:
            self.find_element(*locator).send_keys(text)
        except Exception as e:
            logger.error("Failed to type in input box with %s" % e)
            self.get_screent_img()

    def tap(self, positions, timeout=500):
        logger.info("tap positions % s" % positions)
        try:
            self.driver.tap(positions, timeout)
        except Exception as e:
            logger.info(e)

    @staticmethod
    def sleep(sleep_time):
        """显式等待"""
        logger.info("sleep %s seconds" % sleep_time)
        return time.sleep(sleep_time)

    def get_element_text(self, locator):
        """获取元素的文本"""
        element = self.find_element(*locator)
        element.text

    def get_screen_size(self):
        """获取屏幕分辨率"""
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def swipe_up(self, duration=1000):
        """屏幕向上滑动"""
        logger.info("slide up the screen")
        size = self.get_screen_size()
        x1 = int(size[0] * 0.5)
        y1 = int(size[1] * 0.75)
        y2 = int(size[1] * 0.25)
        self.driver.swipe(x1, y1, x1, y2, duration)

    def swipe_left(self, duration=1000):
        """屏幕向左滑动"""
        logger.info("slide left the screen")
        size = self.get_screen_size()
        x1 = int(size[0] * 0.75)
        y1 = int(size[1] * 0.5)
        x2 = int(size[1] * 0.05)
        self.driver.swipe(x1, y1, x2, y1, duration)

    def swipe_down(self, duration=1000):
        """屏幕向下滑动"""
        logger.info("slide down the screen")
        size = self.get_screen_size()
        x1 = int(size[0] * 0.5)
        y1 = int(size[1] * 0.25)
        y2 = int(size[1] * 0.75)
        self.driver.swipe(x1, y1, x1, y2, duration)

    def swipe_right(self, duration=1000):
        """屏幕向右滑动"""
        logger.info("slide right the screen")
        size = self.get_screen_size()
        x1 = int(size[0] * 0.05)
        y1 = int(size[1] * 0.5)
        x2 = int(size[1] * 0.75)
        self.driver.swipe(x1, y1, x2, y1, duration)

    def click_back(self):
        """点击系统返回键KEYCODE_BACK = 4"""
        logger.info("click the back button")
        self.driver.press_keycode(4)

    def click_home(self):
        """点击系统返回键KEYCODE_HOME = 3"""
        logger.info("click the home button")
        self.driver.press_keycode(3)

    def click_power(self):
        """点击系统电源KEYCODE_POWER = 26"""
        logger.info("click the power button")
        self.driver.press_keycode(26)

    def is_displayed(self, locator):
        """判断元素是否在当前页面显示"""
        try:
            element = self.find_element(*locator)
            return element.is_displayed()
        except NoSuchElementException as e:
            logger.info("Not exist this element %s" % e)

    def is_exist_current(self, text):
        """通过获取所有元素来判断当前text是否存在"""
        all_element = self.driver.page_source
        if text in all_element:
            return True
        else:
            logger.info("Current page not exist %s" % text)
            return False

    def long_press(self, locator, duration=3000):
        """长按"""
        logger.info("long press % s" % locator)
        element = self.find_element(*locator)
        touch_action = TouchAction(self.driver)
        touch_action.long_press(element, duration).perform()

    def hide_keyboard(self):
        """隐藏软键盘"""
        logger.info("hide the keyboard")
        self.driver.hide_keyboard()

    def get_screen_shot(self, case_name):
        """截图"""
        file_name = self.get_current_time() + '_' + case_name
        file_path = BaseUtil().get_root_path() + '/screenshots/%s.png' % file_name
        self.driver.get_screenshot_as_file(file_path)
        return file_path

    def launch_app(self):
        """启动app"""
        logger.info("launch the app")
        self.driver.launch_app()

    def close_app(self):
        """关闭app"""
        logger.info("close the app")
        self.driver.close_app()

    def quit(self):
        """退出driver"""
        logger.info("quit the driver")
        self.driver.quit()

    def assert_in(self, text):
        """text文本在当前页显示，让其断言不通过截图"""
        self.assert_true(self.is_exist_current(text))

    def assert_not_in(self, text):
        """text文本不在当前页显示，让其断言不通过截图"""
        self.assert_false(self.is_exist_current(text))

    def assert_equal(self, value1, value2):
        """相等断言，让其断言不通过截图"""
        try:
            assert value1 == value2, "%s != %s" % (repr(value1), repr(value2))
        except Exception as msg:
            file = self.get_screen_shot(str(inspect.stack()[1][3]))
            content = open(file, 'rb').read()
            allure.MASTER_HELPER.attach('截图', content, type=allure.MASTER_HELPER.attach_type.PNG)
            raise AssertionError(msg)

    def assert_not_equal(self, value1, value2):
        """不相等断言，让其断言不通过截图"""
        try:
            assert value1 != value2, "%s != %s" % (repr(value1), repr(value2))
        except Exception as msg:
            file = self.get_screen_shot(str(inspect.stack()[1][3]))
            content = open(file, 'rb').read()
            allure.MASTER_HELPER.attach('截图', content, type=allure.MASTER_HELPER.attach_type.PNG)
            raise AssertionError(msg)

    def assert_true(self, value):
        """二次封装为真断言，让其断言不通过截图"""
        try:
            assert value is True, "%s is not true" % str(value)
        except Exception as msg:
            file = self.get_screen_shot(str(inspect.stack()[1][3]))
            content = open(file, 'rb').read()
            allure.MASTER_HELPER.attach('截图', content, type=allure.MASTER_HELPER.attach_type.PNG)
            raise AssertionError(msg)

    def assert_false(self, value):
        """真断言，让其断言不通过截图"""
        try:
            assert value is False, "%s is not false" % str(value)
        except Exception as msg:
            file = self.get_screen_shot(str(inspect.stack()[1][3]))
            content = open(file, 'rb').read()
            allure.MASTER_HELPER.attach('截图', content, type=allure.MASTER_HELPER.attach_type.PNG)
            raise AssertionError(msg)

    def is_toast_show(self, message, wait=10):
        """Android检查是否有对应Toast显示,用于断言"""
        locator = {'name': '[Toast] %s' % message, 'timeOutInSeconds': wait, 'type': 'xpath',
                   'value': '//*[contains(@text,\'%s\')]' % message}
        try:
            element = self.find_element(*locator)
            return element is not None
        except NoSuchElementException:
            logger.info("[Toast] can't be found: %s" % locator)
            return False

    @staticmethod
    def get_current_time():
        """获取当前时间"""
        temp = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
        return temp
