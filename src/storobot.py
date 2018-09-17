#!/usr/bin/python

import json
import operator
import time
from pprint import pprint

from selenium import webdriver

from src.events import *
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
            self.tests.append(Test(key, val['order'], val['events'], val['expected_result'], val['url']))
        self.tests = sorted(self.tests, key=operator.attrgetter('order'))

    def get_driver(self, name):
        if name == 'chrome':
            return webdriver.Chrome()
        elif name == 'firefox':
            return webdriver.Firefox()

        return False

    def open(self):
        self.driver.get(self.config['base_url'])

    def close(self):
        self.driver.close()

    def run(self):
        for driver_name in config['drivers']:
            self.driver = self.get_driver(driver_name)
            self.open()
            for test in self.tests:
                event = None
                try:
                    self.driver.get(test.url)
                    for event in test.events:
                        if event['type'] == 'click':
                            click(self.driver, event)
                        elif event['type'] == 'sendkeys':
                            send_keys(self.driver, event)
                        elif event['type'] == 'submit':
                            submit(self.driver, event)
                        elif event['type'] == 'sleep':
                            time.sleep(int(event['value']))
                        elif event['type'] == 'hover':
                            hover(self.driver, event)
                    time.sleep(5)
                    self.results.append(test.assert_result(self.driver))
                except Exception as e:  # log any and all exceptions that occur during tests
                    self.exceptions.append(
                        {'test': test.name, 'driver': self.driver.name, 'event': event, 'exception': repr(e)})
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

        failed = [result for result in self.results if
                  any(assertion['pass'] == False for assertion in result['assertions'])]
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
