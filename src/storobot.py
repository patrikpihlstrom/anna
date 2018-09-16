#!/usr/bin/python

import json
from pprint import pprint

from selenium import webdriver


class Storobot:
    config = None
    driver = None
    tests = None

    def __init__(self, config, tests):
        self.config = config
        self.tests = tests

    def get_driver(self):
        driver = self.config['driver']
        if driver == 'chrome':
            return webdriver.Chrome()
        elif driver == 'firefox':
            return webdriver.Firefox()

        return False

    def open(self):
        self.driver = self.get_driver()
        self.driver.get(self.config['base_url'])

    def close(self):
        self.driver.close()

    def get_element(self, target):
        if 'id' in target:
            element = self.driver.find_element_by_id(target['id'])
        elif 'class' in target:
            element = self.driver.find_elements_by_class_name(target['class'])[0]
        elif 'href' in target:
            element = self.driver.find_element_by_xpath("//a[@href='" + target['href'] + "']")
        return element

    def send_keys(self, event):
        element = self.get_element(event['target'])
        v = event['value'].encode('ascii', 'ignore').decode("utf-8")
        element.send_keys(v)

    def submit(self, event):
        element = self.get_element(event['target'])
        element.submit()

    def click(self, event):
        element = self.get_element(event['target'])
        element.click()

    def run(self):
        self.open()
        for key, test in tests.items():
            for event in test['events']:
                if (event['type'] == 'click'):
                    self.click(event)
                elif (event['type'] == 'sendkeys'):
                    self.send_keys(event)
                elif (event['type'] == 'submit'):
                    self.submit(event)

if __name__ == '__main__':
    config = None
    tests = None
    with open('../config.json') as config:
        config = json.load(config)

    with open('../tests.json') as tests:
        tests = json.load(tests)
        for driver in config['drivers']:
            config['driver'] = driver
            robot = Storobot(config, tests)
            robot.run()
