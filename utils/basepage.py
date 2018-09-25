#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import inspect
import time
import allure
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *
from utils.log import Logger

logger = Logger(logger='BasePage').get_log()


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@singleton
class BasePage(object):
    """
    ########################################
    描述：封装元素的基本操作
        包括元素定位、点击、输入文本、清除文本框、
        获取元素的text内容、滑动、Touch操作、
        系统按键的操作
    属性：
    ########################################
    """

    def __init__(self, driver):
        """
        ########################################
        描述：初始化方法
        参数：none
        返回值：none
        异常描述：none
        ########################################
        """
        self.driver = driver
        self.width = self.driver.get_window_size()['width']
        self.height = self.driver.get_window_size()['height']
        self.timeout_time = 15
        self.wait_time = 2

    def reset(self):
        """
        ########################################
        描述：因为是单例,所以当driver变动的时候,需要重置一下driver
        参数：driver: driver
        返回值：none
        异常描述：self
        ########################################
        """
        self.width = self.driver.get_window_size()['width']
        self.height = self.driver.get_window_size()['height']
        return self

    def find_element(self, type_and_value):
        """
        ########################################
        描述：定位单个元素
        参数：by:通过什么方法来定位
        返回值：none
        异常描述：none
        ########################################
        """
        if ">=" not in type_and_value:
            by = "id"
            value = type_and_value
        else:
            attr = type_and_value.split(">=")
            by = attr[0]
            value = attr[1]
        try:
            if by == "id":
                WebDriverWait(self.driver, self.timeout_time).until(
                    lambda driver: driver.find_element_by_id(value).is_displayed())
                self.driver.implicitly_wait(self.wait_time)
                element = self.driver.find_element_by_id(value)
                return element
            if by == "name":
                find_name = "//*[@text='%s']" % value
                WebDriverWait(self.driver, self.timeout_time).until(
                    lambda driver: driver.find_element_by_xpath(find_name).is_displayed())
                self.driver.implicitly_wait(self.wait_time)
                element = self.driver.find_element_by_xpath(find_name)
                return element
            if by == "xpath":
                WebDriverWait(self.driver, self.timeout_time).until(
                    lambda driver: driver.find_element_by_xpath(value).is_displayed())
                self.driver.implicitly_wait(self.wait_time)
                element = self.driver.find_element_by_xpath(value)
                return element
            if by == "class":
                WebDriverWait(self.driver, self.timeout_time).until(
                    lambda driver: driver.find_element_by_class_name(value).is_displayed())
                self.driver.implicitly_wait(self.wait_time)
                element = self.driver.find_element_by_class_name(value)
                return element
            if by == "content":
                WebDriverWait(self.driver, self.timeout_time).until(
                    lambda driver: driver.find_element_by_accessibility_id(value).is_displayed())
                self.driver.implicitly_wait(self.wait_time)
                element = self.driver.find_element_by_accessibility_id(value)
                return element
            else:
                raise NameError("Please Enter correct element value")
        except NoSuchElementException:
            logger.info("Can not find element: %s" % type_and_value)
            raise

    def find_elements(self, by, value):
        """
        ########################################
        描述：定位一组元素
        参数：by:通过什么方法来定位
        返回值：none
        异常描述：none
        ########################################
        """
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
            logger.info("Can not find elements: %s" % value)
            raise

    def click(self, locator):
        """
        ########################################
        描述：封装点击
        参数：value:元素类型和值的组合字符串
        返回值：none
        异常描述：none
        ########################################
        """
        logger.info("click element: %s" % locator)
        element = self.find_element(locator)
        element.click()

    def input_text(self, locator, text):
        """
        ########################################
        描述：在文本框输入文本
        参数：value:元素类型和值的组合字符串
            text:输入的文本
        返回值：none
        异常描述：none
        ########################################
        """
        element = self.find_element(locator)
        element.send_keys(text)

    def clear_input(self, locator):
        """
        ########################################
        描述：清除文本框
        参数：value:元素类型和值的组合字符串
        返回值：none
        异常描述：none
        ########################################
        """
        element = self.find_element(locator)
        element.clear()

    @staticmethod
    def sleep(sleep_time):
        """
        ########################################
        描述：显示等待
        参数：sleep_time:等待时间
        返回值：等待时间
        异常描述：none
        ########################################
        """
        return time.sleep(sleep_time)

    def get_element_text(self, locator):
        """
        ########################################
        描述：获取元素的文本
        参数：value:元素类型和值的组合字符串
        返回值：none
        异常描述：none
        ########################################
        """
        element = self.find_element(locator)
        element.text

    def get_screen_size(self):
        """
        ########################################
        描述：获取屏幕分辨率
        参数：none
        返回值：none
        异常描述：none
        ########################################
        """
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def swipe_up(self, duration=1000):
        """
        ########################################
        描述：屏幕向上滑动
        参数：duration:滑动时间
        返回值：none
        异常描述：none
        ########################################
        """
        size = self.get_screen_size()
        x1 = int(size[0] * 0.5)
        y1 = int(size[1] * 0.75)
        y2 = int(size[1] * 0.25)
        self.driver.swipe(x1, y1, x1, y2, duration)

    def swipe_left(self, duration=1000):
        """
        ########################################
        描述：屏幕向左滑动
        参数：duration:滑动时间
        返回值：none
        异常描述：none
        ########################################
        """
        size = self.get_screen_size()
        x1 = int(size[0] * 0.75)
        y1 = int(size[1] * 0.5)
        x2 = int(size[1] * 0.05)
        self.driver.swipe(x1, y1, x2, y1, duration)

    def swipe_down(self, duration=1000):
        """
        ########################################
        描述：屏幕向下滑动
        参数：duration:滑动时间
        返回值：none
        异常描述：none
        ########################################
        """
        size = self.get_screen_size()
        x1 = int(size[0] * 0.5)
        y1 = int(size[1] * 0.25)
        y2 = int(size[1] * 0.75)
        self.driver.swipe(x1, y1, x1, y2, duration)

    def swipe_right(self, duration=1000):
        """
        ########################################
        描述：屏幕向右滑动
        参数：duration:滑动时间
        返回值：none
        异常描述：none
        ########################################
        """
        size = self.get_screen_size()
        x1 = int(size[0] * 0.05)
        y1 = int(size[1] * 0.5)
        x2 = int(size[1] * 0.75)
        self.driver.swipe(x1, y1, x2, y1, duration)

    def click_back(self):
        """
        ########################################
        描述：点击系统返回键KEYCODE_BACK = 4
        参数：none
        返回值：none
        异常描述：none
        ########################################
        """
        self.driver.press_keycode(4)

    def click_home(self):
        """
        ########################################
        描述：点击系统返回键KEYCODE_HOME = 3
        参数：none
        返回值：none
        异常描述：none
        ########################################
        """
        self.driver.press_keycode(3)

    def click_power(self):
        """
        ########################################
        描述：点击系统返回键KEYCODE_POWER = 26
        参数：none
        返回值：none
        异常描述：none
        ########################################
        """
        self.driver.press_keycode(26)

    def is_displayed(self, locator):
        """
        ########################################
        描述：判断元素是否在当前页面显示
        参数：value:元素类型和值的组合字符串
        返回值：返回显示/未显示 true/false
        异常描述：none
        ########################################
        """
        element = self.find_element(locator)
        return element.is_displayed()

    def is_exist_current(self, text):
        """
        ########################################
        描述：通过获取所有元素来判断当前text是否存在
        参数：text：需要判断的元素text
        返回值：none
        异常描述：none
        ########################################
        """
        all_element = self.driver.page_source
        return text in all_element

    def long_press(self, locator, duration=3000):
        """
        ########################################
        描述：长按
        参数：value:元素类型和值的组合字符串，duration:持续时间
        返回值：none
        异常描述：none
        ########################################
        """
        element = self.find_element(locator)
        touch_action = TouchAction(self.driver)
        touch_action.long_press(element, duration).perform()

    def hide_keyboard(self):
        """
        ########################################
        描述：隐藏软键盘
        参数：none
        返回值：none
        异常描述：none
        ########################################
        """
        self.driver.hide_keyboard()

    def get_screen_shot(self, case_name):
        """
        ########################################
        描述：截图
        参数：case_name: 当前case名称
        返回值：none
        异常描述：none
        ########################################
        """
        file_name = self.format_screen_shot_time() + '_' + case_name
        file_path = '../android_project/screenshot/%s.png' % file_name
        self.driver.get_screenshot_as_file(file_path)
        return file_path

    def launch(self):
        """
        ########################################
        描述：启动app
        参数：none
        返回值：none
        异常描述：none
        ########################################
        """
        self.driver.launch_app()

    def close(self):
        """
        ########################################
        描述：关闭app
        参数：none
        返回值：none
        异常描述：none
        ########################################
        """
        self.driver.close_app()

    def quit(self):
        self.driver.quit()

    def assert_in(self, text):
        """
        ########################################
        描述：text文本在当前页显示，让其断言不通过截图
        参数：none
        返回值：none
        异常描述：none
        ########################################
        """
        self.assert_true(self.is_exist_current(text))

    def assert_not_in(self, text):
        """
        ########################################
        描述：text文本不在当前页显示，让其断言不通过截图
        参数：none
        返回值：none
        异常描述：none
        ########################################
        """
        self.assert_false(self.is_exist_current(text))

    def assert_equal(self, value1, value2):
        """
        ########################################
        描述：相等断言，让其断言不通过截图
        参数：none
        返回值：none
        异常描述：none
        ########################################
        """
        try:
            assert value1 == value2, "%s != %s" % (repr(value1), repr(value2))
        except Exception as msg:
            file = self.get_screen_shot(str(inspect.stack()[1][3]))
            content = open(file, 'rb').read()
            allure.MASTER_HELPER.attach('截图', content, type=allure.MASTER_HELPER.attach_type.PNG)
            raise AssertionError(msg)

    def assert_not_equal(self, value1, value2):
        """
        ########################################
        描述：不相等断言，让其断言不通过截图
        参数：none
        返回值：none
        异常描述：none
        ########################################
        """
        try:
            assert value1 != value2, "%s != %s" % (repr(value1), repr(value2))
        except Exception as msg:
            file = self.get_screen_shot(str(inspect.stack()[1][3]))
            content = open(file, 'rb').read()
            allure.MASTER_HELPER.attach('截图', content, type=allure.MASTER_HELPER.attach_type.PNG)
            raise AssertionError(msg)

    def assert_true(self, value):
        """
        ########################################
        描述：2次封装为真断言，让其断言不通过截图
        参数：none
        返回值：none
        异常描述：none
        ########################################
        """
        try:
            assert value is True, "%s is not true" % str(value)
        except Exception as msg:
            file = self.get_screen_shot(str(inspect.stack()[1][3]))
            content = open(file, 'rb').read()
            allure.MASTER_HELPER.attach('截图', content, type=allure.MASTER_HELPER.attach_type.PNG)
            raise AssertionError(msg)

    def assert_false(self, value):
        """
        ########################################
        描述：真断言，让其断言不通过截图
        参数：none
        返回值：none
        异常描述：none
        ########################################
        """
        try:
            assert value is False, "%s is not false" % str(value)
        except Exception as msg:
            file = self.get_screen_shot(str(inspect.stack()[1][3]))
            content = open(file, 'rb').read()
            allure.MASTER_HELPER.attach('截图', content, type=allure.MASTER_HELPER.attach_type.PNG)
            raise AssertionError(msg)

    def is_toast_show(self, message, wait=10):
        """
        ########################################
        描述：Android检查是否有对应Toast显示,用于断言
        参数：message: Toast信息
             wait:  等待时间,默认10秒
        返回值：True 显示 Toast信息
        异常描述：NoSuchElementException
        ########################################
        """
        locator = {'name': '[Toast] %s' % message, 'timeOutInSeconds': wait, 'type': 'xpath',
                   'value': '//*[contains(@text,\'%s\')]' % message}
        try:
            element = self.find_element(locator)
            return element is not None
        except NoSuchElementException:
            logger.info("[Toast] can't be found: %s" % locator)
            return False

    @staticmethod
    def format_screen_shot_time():
        """
        ########################################
        描述：格式化屏幕截图时间，用于文件名
        参数：none
        返回值：返回格式化的时间
        异常描述：none
        ########################################
        """
        temp = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
        return temp
