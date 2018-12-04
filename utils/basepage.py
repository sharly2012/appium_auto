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
        """init"""
        self.driver = driver
        self.width = self.driver.get_window_size()['width']
        self.height = self.driver.get_window_size()['height']
        self.timeout_time = 15
        self.wait_time = 2

    def reset(self):
        """reset driver"""
        logger.info("reset the driver ...")
        self.width = self.driver.get_window_size()['width']
        self.height = self.driver.get_window_size()['height']
        return self

    def find_element(self, *locator):
        """find the element"""
        try:
            WebDriverWait(self.driver, 30, 0.5).until(lambda driver: driver.find_element(*locator).is_displayed())
            return self.driver.find_element(*locator)
        except NoSuchElementException:
            logger.warning('Can not find element: %s' % locator[1])
            raise
        except TimeoutException:
            logger.warning('Can not find element: %s' % locator[1])

    def find_elements(self, by, value):
        """find elements"""
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
        """click"""
        logger.info('Click element by %s: %s ...' % (locator[0], locator[1]))
        try:
            self.find_element(*locator).click()
        except AttributeError as e:
            logger.warning("The element is unclickable: %s" % e)

    def clear_input(self, locator):
        """clear the input"""
        element = self.find_element(*locator)
        try:
            element.clear()
            logger.info('Clear input-box by %s: %s ...' % (locator[0], locator[1]))
        except NameError as ne:
            logger.warning("Failed to clear in input box with %s" % ne)

    def send_keys(self, locator, text):
        """send keys"""
        self.find_element(*locator).clear()
        logger.info('Input element by %s : %s values %s ...' % (locator[0], locator[1], text))
        try:
            self.find_element(*locator).send_keys(text)
        except Exception as e:
            logger.error("Failed to type in input box with %s" % e)

    def tap(self, positions, timeout=500):
        """tap element"""
        logger.info("Tap positions %s ..." % positions)
        try:
            self.driver.tap(positions, timeout)
        except Exception as e:
            logger.info(e)

    @staticmethod
    def sleep(sleep_time):
        """sleep"""
        logger.info("sleep %s seconds" % sleep_time)
        return time.sleep(sleep_time)

    def get_element_text(self, locator):
        """get the element text"""
        try:
            element = self.find_element(*locator)
            element.text
        except Exception as e:
            logger.info("Can't get the text of %s" % locator)
            logger.error(e)

    def get_screen_size(self):
        """get the mobile screen size"""
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def swipe_up(self, duration=1000):
        """swipe up"""
        logger.info("slide up the screen ...")
        size = self.get_screen_size()
        x1 = int(size[0] * 0.5)
        y1 = int(size[1] * 0.75)
        y2 = int(size[1] * 0.25)
        self.driver.swipe(x1, y1, x1, y2, duration)

    def swipe_left(self, duration=1000):
        """swipe left"""
        logger.info("slide left the screen ...")
        size = self.get_screen_size()
        x1 = int(size[0] * 0.75)
        y1 = int(size[1] * 0.5)
        x2 = int(size[1] * 0.05)
        self.driver.swipe(x1, y1, x2, y1, duration)

    def swipe_down(self, duration=1000):
        """swipe down"""
        logger.info("slide down the screen ...")
        size = self.get_screen_size()
        x1 = int(size[0] * 0.5)
        y1 = int(size[1] * 0.25)
        y2 = int(size[1] * 0.75)
        self.driver.swipe(x1, y1, x1, y2, duration)

    def swipe_right(self, duration=1000):
        """swipe right"""
        logger.info("slide right the screen ...")
        size = self.get_screen_size()
        x1 = int(size[0] * 0.05)
        y1 = int(size[1] * 0.5)
        x2 = int(size[1] * 0.75)
        self.driver.swipe(x1, y1, x2, y1, duration)

    def click_back(self):
        """click the back button, KEYCODE_BACK = 4"""
        logger.info("click the back button ...")
        self.driver.press_keycode(4)

    def click_home(self):
        """click the home button, KEYCODE_HOME = 3"""
        logger.info("click the home button ...")
        self.driver.press_keycode(3)

    def click_power(self):
        """click the power button, KEYCODE_POWER = 26"""
        logger.info("click the power button ...")
        self.driver.press_keycode(26)

    def is_displayed(self, locator):
        """verify the element is or not exist"""
        try:
            element = self.find_element(*locator)
            return element.is_displayed()
        except NoSuchElementException as e:
            logger.info("Not exist this element %s" % e)

    def is_exist_current(self, text):
        """verify the text is or not in the page source"""
        all_element = self.driver.page_source
        if text in all_element:
            return True
        else:
            logger.info("Current page not exist %s" % text)
            return False

    def long_press(self, locator, duration=3000):
        """long press"""
        logger.info("long press % s" % locator)
        element = self.find_element(*locator)
        touch_action = TouchAction(self.driver)
        touch_action.long_press(element, duration).perform()

    def hide_keyboard(self):
        """hide the keyboard"""
        logger.info("hide the keyboard ...")
        self.driver.hide_keyboard()

    def get_screen_shot(self, case_name):
        """screen shot"""
        file_name = self.get_current_time() + '_' + case_name
        file_path = BaseUtil().get_root_path() + '/screenshots/%s.png' % file_name
        self.driver.get_screenshot_as_file(file_path)
        return file_path

    def launch_app(self):
        """launch the app"""
        logger.info("launch the app ...")
        self.driver.launch_app()

    def close_app(self):
        """close the app"""
        logger.info("close the app ...")
        self.driver.close_app()

    def quit(self):
        """quit the driver"""
        logger.info("quit the driver ...")
        self.driver.quit()

    def assert_in(self, text):
        """verify the current page exist the text, or it will be fail"""
        self.assert_true(self.is_exist_current(text))
        logger.info("Current page not exist %s, fail" % text)

    def assert_not_in(self, text):
        """verify the current page not exist the text, or it will be fail"""
        self.assert_false(self.is_exist_current(text))
        logger.info("Current page exist %s, fail" % text)

    def assert_equal(self, value1, value2):
        """assert equal, or it will be fail"""
        try:
            assert value1 == value2, "%s != %s" % (repr(value1), repr(value2))
        except Exception as msg:
            file = self.get_screen_shot(str(inspect.stack()[1][3]))
            content = open(file, 'rb').read()
            allure.MASTER_HELPER.attach('screen shot', content, type=allure.MASTER_HELPER.attach_type.PNG)
            logger.error(msg)

    def assert_not_equal(self, value1, value2):
        """assert not equal, or it will be fail"""
        try:
            assert value1 != value2, "%s != %s" % (repr(value1), repr(value2))
        except Exception as msg:
            file = self.get_screen_shot(str(inspect.stack()[1][3]))
            content = open(file, 'rb').read()
            allure.MASTER_HELPER.attach('screen shot', content, type=allure.MASTER_HELPER.attach_type.PNG)
            logger.error(msg)

    def assert_true(self, value):
        """assert true, or it will be fai"""
        try:
            assert value is True, "%s is not true" % str(value)
        except Exception as msg:
            file = self.get_screen_shot(str(inspect.stack()[1][3]))
            content = open(file, 'rb').read()
            allure.MASTER_HELPER.attach('screen shot', content, type=allure.MASTER_HELPER.attach_type.PNG)
            logger.error(msg)

    def assert_false(self, value):
        """assert false, or it will be fai"""
        try:
            assert value is False, "%s is not false" % str(value)
        except Exception as msg:
            file = self.get_screen_shot(str(inspect.stack()[1][3]))
            content = open(file, 'rb').read()
            allure.MASTER_HELPER.attach('screen shot', content, type=allure.MASTER_HELPER.attach_type.PNG)
            logger.error(msg)

    def is_toast_show(self, message, wait=10):
        """check the toast show and use to assert"""
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
