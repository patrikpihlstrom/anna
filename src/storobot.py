#!/usr/bin/python

import json
import operator
import sys
import time
from pprint import pprint

from selenium import webdriver

from src.test import Test


class Storobot:
    config = None
    driver = None
    tests = []
    results = []
    exceptions = []

    def __init__(self, config, tests):
        self.config = config
        for key, val in tests.items():
            self.tests.append(Test(key, val['order'], val['events'], val['expected_result']))
        self.tests = sorted(self.tests, key=operator.attrgetter('order'))

    def get_driver(self, name):
        if name== 'chrome':
            return webdriver.Chrome()
        elif name == 'firefox':
            return webdriver.Firefox()

        return False

    def open(self):
        self.driver.get(self.config['base_url'])

    def close(self):
        self.driver.close()

    def get_element(self, target):
        try:
            if 'id' in target:
                element = self.driver.find_element_by_id(target['id'])
            elif 'class' in target:
                    element = self.driver.find_elements_by_class_name(target['class'])[0]
            elif 'href' in target:
                element = self.driver.find_element_by_xpath("//a[@href='" + target['href'] + "']")
        except:
            return False
        return element

    def send_keys(self, event):
        element = self.get_element(event['target'])
        if element != False:
            v = event['value'].encode('ascii', 'ignore').decode("utf-8")
            element.send_keys(v)

    def submit(self, event):
        element = self.get_element(event['target'])
        if element != False:
            element.submit()

    def click(self, event):
        element = self.get_element(event['target'])
        if element != False:
            element.click()

    def run(self):
        for driver_name in config['drivers']:
            self.driver = self.get_driver(driver_name)
            self.open()
            for test in self.tests:
                event = None
                try:
                    for event in test.events:
                        if (event['type'] == 'click'):
                            self.click(event)
                        elif (event['type'] == 'sendkeys'):
                            self.send_keys(event)
                        elif (event['type'] == 'submit'):
                            self.submit(event)
                    time.sleep(5)
                    self.results.append(test.assert_result(self.driver))
                except:
                    self.exceptions.append({'name': test.name, 'event': event, 'exception': str(sys.exc_info()[0])})
                    pass
            self.close()
        self.print_results()

    def loaded(self):
        state = self.driver.execute_script('return document.readyState;')
        return state == 'complete'

    def print_results(self):
        if len(self.exceptions) > 0:
            print('Exceptions: ')
            pprint(self.exceptions)

        failed = [result for result in self.results if any(assertion['pass'] == False for assertion in result['assertions'])]
        if len(failed) > 0:
            pprint(failed)
        elif len(self.exceptions) == 0:
            print('All tests passed successfully!')


if __name__ == '__main__':
    config = None
    tests = None
    with open('../config.json') as config:
        config = json.load(config)

    with open('../tests.json') as tests:
        tests = json.load(tests)
        robot = Storobot(config, tests)
        robot.run()
