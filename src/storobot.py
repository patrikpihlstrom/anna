#!/usr/bin/python

import json
import time
from pprint import pprint

from selenium import webdriver

from src.events import *
from src.test import Test


class Storobot:
    config = None
    driver = None
    tests = {}
    sequence = []
    results = []
    exceptions = []

    def __init__(self, config, tests):
        self.config = config
        for url, site in tests.items():
            self.tests[url] = {}
            for key, val in site['tests'].items():
                self.tests[url][key] = Test(key, val['events'], val['expected_result'], url, config['sites'])
            for order in sorted(site['sequence']):
                self.sequence.append(site['sequence'][order])

    def get_driver(self, name):
        if name == 'chrome':
            return webdriver.Chrome()
        elif name == 'firefox':
            return webdriver.Firefox()

        return False

    def open(self, base_url):
        self.driver.get(base_url)

    def close(self):
        self.driver.close()

    def run_test(self, site, test):
        event = None
        try:
            for event in test.events:
                if isinstance(event, str):
                    sub_test = event.lstrip('@')
                    if sub_test in self.tests[site]:
                        sub_test = self.tests[site][sub_test]
                    if isinstance(sub_test, Test):
                        self.run_test(site, sub_test)
                else:
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
                    elif event['type'] == 'wait':
                        wait(self.driver, event)
                time.sleep(1)
            self.results.append(test.assert_result(self.driver))
        except Exception as e:  # log any and all exceptions that occur during tests
            self.exceptions.append(
                {'test': test.name, 'driver': self.driver.name, 'event': event, 'exception': repr(e)})
            pass

    def run(self):
        for site, config in self.config['sites'].items():
            for driver_name in self.config['drivers']:
                self.driver = self.get_driver(driver_name)
                self.open(site)
                for test in self.sequence:
                    self.run_test(site, self.tests[site][test])
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
                  any(not assertion['pass'] for assertion in result['assertions'])]
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
