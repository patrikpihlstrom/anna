#!/usr/bin/python

import json
from pprint import pprint

from selenium import webdriver

import src.events as events
from src.test import Test


class Magebot:
    config = driver = None
    sequence = []
    results = []
    exceptions = []
    tests = {}

    def __init__(self, config, tests):
        self.config = config
        for url, site in tests.items():
            self.tests[url] = {}
            for key, val in site['tests'].items():
                self.tests[url][key] = Test(key, val['events'], val['expected_result'], url, config['sites'])
            for order in sorted(site['sequence']):
                self.sequence.append(site['sequence'][order])

    @staticmethod
    def get_driver(name):
        if name == 'chrome':
            return webdriver.Chrome()
        elif name == 'firefox':
            return webdriver.Firefox()
        elif name == 'ie':
            return webdriver.Ie()
        elif name == 'edge':
            return webdriver.Edge()
        return False

    def open(self, base_url):
        self.driver.get(base_url)

    def close(self):
        self.driver.close()

    def run_test(self, test):
        event = None
        try:
            for event in test.events:
                func = getattr(events, event['type'])
                func(self.driver, event)

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
                    self.run_test(self.tests[site][test])
                self.close()
        self.print_results()

    def print_results(self):
        if len(self.exceptions) > 0:
            print('Exceptions: ')
            pprint(self.exceptions)

        failed = [result for result in self.results if
                  any(not assertion['pass'] for assertion in result['assertions'])]  # list comprehension <3
        if len(failed) > 0:
            pprint(failed)
        elif len(self.exceptions) == 0:
            print('All tests passed successfully!')


if __name__ == '__main__':
    with open('../config.json') as config:
        config = json.load(config)

    with open('../tests.json') as tests:
        tests = json.load(tests)
        robot = Magebot(config, tests)
        robot.run()
