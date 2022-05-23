# coding=utf-8

import sys

sys.path.append("d:\\Test\\pythonProject\\new\\logger")

import time
import os
from selenium.common.exceptions import NoSuchElementException
import logger


class BasePage:
    def __init__(self, driver):
        """define browser"""
        self.driver = driver
        self.log = logger.Logger().get_log()

    def quit_browser(self):
        """End test with quitting browser"""
        self.driver.quit()
        self.log.info("Browser has been quitted")

    def forward_browser(self):
        """define forward action"""
        self.driver.forward()
        self.log.info("Browser has forwarded")

    def back_browser(self):
        """define back action"""
        self.driver.back()
        self.log.info("Browser has backed")

    def wait(self, seconds):
        """define implicitly wait time"""
        self.driver.implicitly_wait(seconds)
        self.log.info("Implicitly waiting for %d seconds" % seconds)

    def close_browser(self):
        """define close browser"""
        self.driver.close()
        self.log.info("Close Browser")

    def get_screen_image(self):
        """define getting screenshot"""
        file_path = os.path.join(os.path.dirname(os.path.abspath('.')), 'screenshots')
        current_time = time.strftime("%Y%m%d%H%M%S")
        image_name = os.path.join(file_path, "%s.png" % current_time)
        try:
            self.driver.get_screenshot_as_file(image_name)
            self.log.info("Taking a screenshot and saving to folder: /screenshots'")
        except NameError as e:
            self.log.error("Fail to take screenshot! %s" % e)

    def find_element(self, *selector):
        """define universal finding element method"""
        try:
            element = self.driver.find_element(*selector)
            self.log.info("The element looked up is %s " % str(selector))
            return element
        except NoSuchElementException as e:
            self.log.error("NoSuchElementException: %s" % e)
            self.get_screen_image()
        self.wait(10)

    def type(self, text, *selector):
        """define typing"""
        el = self.find_element(*selector)
        el.clear()
        try:
            el.send_keys(text)
            self.log.info("typing \' %s \' in inputBox" % text)
        except NameError as e:
            self.log.error("Failed to type in input box with %s" % e)
            self.get_screen_image()
        self.wait(10)

    def click_on(self, *selector):
        """define click action"""
        el = self.find_element(*selector)
        try:
            el.click()
            self.log.info("The element \' %s \' was clicked." % el.text)
        except NameError as e:
            self.log.error("Failed to click the element with %s" % e)
            self.get_screen_image()
        self.wait(10)

    def get_page_title(self):
        """define getting page title"""
        self.log.info("Current page title is %s" % self.driver.title)
        return self.driver.title

    @staticmethod
    def sleep(seconds):
        """define sleep action"""
        time.sleep(seconds)
        logger.Logger().get_log().info("Sleep for %d seconds" % seconds)
