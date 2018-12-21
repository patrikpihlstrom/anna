#!/usr/bin/python

import json, time
from pprint import pprint

import click
from selenium import webdriver

import src.events as events
from src.test_manager import get_tests


class Magebot:
    config = driver = None
    results = []
    exceptions = []
    tests = {}

    def __init__(self, config):
        self.config = config

    @staticmethod
    def get_driver(name):
        if name == 'chrome':
            o = webdriver.ChromeOptions()
            o.headless = True
            return webdriver.Chrome(options=o)
        elif name == 'firefox':
            o = webdriver.FirefoxOptions()
            o.headless = True
            return webdriver.Firefox(options=o)
        elif name == 'ie':
            o = webdriver.IeOptions()
            o.headless = True
            return webdriver.Ie(options=o)
        elif name == 'edge':
            return webdriver.Edge()
        return False

    def close(self):
        self.driver.close()

    def run_test(self, test):
        event = None
        try:
            for event in test.events:
                func = getattr(events, event['type'])
                func(self.driver, event)
            time.sleep(3)
            self.results.append(test.assert_result(self.driver))
        except Exception as e:  # log any and all exceptions that occur during tests
            self.exceptions.append(
                {'test': test.name, 'url': test.url, 'driver': self.driver.name, 'event': event, 'exception': repr(e)})
            pass

    def run(self):
        i = 0
        l = sum([len(self.tests[site]) for site in self.tests])*len(self.config['drivers'])
        with click.progressbar(length=l, label='Running tests') as bar:
            for site in self.tests.keys():
                for driver_name in self.config['drivers']:
                    self.driver = self.get_driver(driver_name)
                    self.driver.get(site)
                    for test in self.tests[site]:
                        self.run_test(test)
                        i += 1
                        bar.update(i)
                    self.close()
        self.print_results()

    def print_results(self):
        if len(self.exceptions) > 0:
            print('Exceptions: ')
            pprint(self.exceptions)
        failed = [result for result in self.results if any(not assertion['pass'] for assertion in result['assertions'])]
        if len(failed) > 0:
            pprint(failed)
        elif len(self.exceptions) == 0:
            print('All tests passed successfully!')

    def set_tests(self, tests):
        self.tests = tests


if __name__ == '__main__':
    with open('../config.json') as config:
        config = json.load(config)

    bot = Magebot(config)
    bot.set_tests(get_tests())
    bot.run()
