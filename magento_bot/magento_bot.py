#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time


class MagentoBot:
    config = None
    driver = None

    def get_driver(self):
        driver = self.config['driver']
        if driver == 'chrome':
            return webdriver.Chrome()
        elif driver == 'firefox':
            return webdriver.Firefox()

        return False

    def __init__(self, config):
        self.config = config

    def open(self):
        self.driver = self.get_driver()
        self.driver.get(self.config['url'])

    def close(self):
        self.driver.close()

