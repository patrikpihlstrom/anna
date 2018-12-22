#!/usr/bin/python

from pprint import pprint
import time

from selenium import webdriver
import term

import src.events as events


class Magebot:
	def __init__(self, config):
		self.config = None
		self.driver = None
		self.tests = {}
		self.exceptions = []
		self.options = []
		self.results = []
		self.config = config

	@staticmethod
	def get_driver(name, options=[]):
		"""
		Returns a new webdriver by the requested name
		pass -h to run in headless mode
		"""
		if name == 'chrome':
			o = webdriver.ChromeOptions()
			o.headless = '-h' in options
			return webdriver.Chrome(options=o)
		elif name == 'firefox':
			o = webdriver.FirefoxOptions()
			o.headless = '-h' in options
			return webdriver.Firefox(options=o)
		elif name == 'ie':
			o = webdriver.IeOptions()
			o.headless = '-h' in options
			return webdriver.Ie(options=o)
		elif name == 'edge':
			return webdriver.Edge()
		return False

	def close(self):
		self.driver.close()

	def run_test(self, test):
		"""
		Run a test and add the result
		:param test:
		:return:
		"""
		if test.name == 'place_order':
			debug = True
		term.writeLine('Running %s@%s on %s' % (test.name, test.url, self.driver.name))
		event = None
		try:
			for event in test.events:
				time.sleep(1)
				func = getattr(events, event['type'])
				func(self.driver, event)
			time.sleep(2)
			result = test.assert_result(self.driver)
			if not any(not assertion['pass'] for assertion in result['assertions']):
				term.writeLine('passed', term.green)
			else:
				term.writeLine('failed', term.red)
			self.results.append(result)
		except Exception as e:  # log any and all exceptions that occur during tests
			term.writeLine(str({'test': test.name, 'url': test.url, 'driver': self.driver.name, 'event': event, 'exception': repr(e)}), term.red)
			self.results.append(test.assert_result(self.driver))
			self.exceptions.append(
				{'test': test.name, 'url': test.url, 'driver': self.driver.name, 'event': event, 'exception': repr(e)})
			pass

	def run(self):
		"""
		Run all tests in all browsers on all sites
		:return:
		"""
		for site in self.tests.keys():
			for driver_name in self.config['drivers']:
				self.driver = self.get_driver(driver_name, self.options)
				self.driver.get(site)
				for test in self.tests[site]:
					self.run_test(test)
				self.close()
		self.print_results()

	def print_results(self):
		if len(self.exceptions) > 0:
			print('Exceptions: ')
			pprint(self.exceptions)
		failed = [result for result in self.results if any(not assertion['pass'] for assertion in result['assertions'])]
		ratio = float(len(failed))/float(len(self.results))
		if len(failed) == 0:
			term.writeLine('%x/%x tests passed' % (len(self.results)-len(failed), len(self.results)), term.green)
		elif ratio < 0.5:
			term.writeLine('%x/%x tests passed' % (len(self.results)-len(failed), len(self.results)), term.yellow)
		else:
			term.writeLine('%x/%x tests passed' % (len(self.results)-len(failed), len(self.results)), term.red)

	def set_tests(self, tests):
		self.tests = tests

	def set_option(self, arg):
		self.options.append(arg)