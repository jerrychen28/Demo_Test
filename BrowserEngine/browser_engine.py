# coding=utf-8

import sys

sys.path.append("d:\\Test\\pythonProject\\new\\logger")

import os.path
from configparser import ConfigParser
from selenium import webdriver
import logger


class BrowserEngine():
    dir = os.path.dirname(os.path.abspath('.'))
    chrome_driver_path = dir + '/tools/chromedriver.exe'
    ie_driver_path = dir + '/tools/IEDriverServer.exe'

    def __init__(self):
        self.log = logger.Logger().get_log()

        # read the browser type from config.ini file, return the driver

    def open_browser(self):
        # read config
        config = ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)

        # get config
        browser = config.get("browserType", "browserName")
        self.log.info("You have selected %s browser." % browser)
        url = config.get("testServer", "URL")
        self.log.info("The test server url is: %s" % url)

        if browser == "Firefox":
            driver = webdriver.Firefox()
            self.log.info("Starting firefox browser.")
        elif browser == "Chrome":
            driver = webdriver.Chrome(self.chrome_driver_path)
            self.log.info("Starting Chrome browser.")
        elif browser == "IE":
            driver = webdriver.Ie(self.ie_driver_path)
            self.log.info("Starting IE browser.")

        driver.get(url)
        self.log.info("Open url: %s" % url)
        driver.maximize_window()
        self.log.info("Maximize the current window.")
        driver.implicitly_wait(10)
        self.log.info("Set implicitly wait 10 seconds.")
        return driver

    def quit_browser(self):
        self.log.info("Now, close and quit the browser.")
        self.driver.quit()
