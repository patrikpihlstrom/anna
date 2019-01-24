#!/usr/bin/python

import time

import driver
import events
import result
import colors


class Magebot:
	def __init__(self, config):
		self.config = None
		self.driver = None
		self.tests = {}
		self.exceptions = []
		self.options = []
		self.config = config
		self.result = result.Result()

	def close(self):
		self.driver.close()

	def run_test(self, test):
		"""
		Run a test and add the result
		:param test:
		:return:
		"""
		print('Running %s @ %s on %s' % (test.name, test.url, self.driver.name))
		event = None
		try:
			for event in test.events:
				time.sleep(1)
				func = getattr(events, event['type'])
				func(self.driver, event)
				time.sleep(1)
			time.sleep(1)
			result = test.assert_result(self.driver)
			if not any(not assertion['pass'] for assertion in result['assertions']):
				print(colors.green + 'passed' + colors.white)
			else:
				print(colors.red + 'failed' + colors.white)
			self.result.append(result)
		except Exception as e:  # log any and all exceptions that occur during tests
			self.result.record_exception(e, test, event, self.options, self.driver)
			pass

	def run(self):
		"""
		Run all tests in all browsers on all sites
		:return:
		"""
		for site in self.tests.keys():
			for driver_name in self.config['drivers']:
				self.driver = driver.get_driver(driver_name, self.options)
				self.driver.get(site)
				for test in self.tests[site]:
					self.run_test(test)
				self.close()
		self.result.print_results(self.options)

	def set_tests(self, tests):
		self.tests = tests

	def set_option(self, arg):
		self.options.append(arg)

	def get_sites(self):
		if any('-s' in option for option in self.options):
			i = self.options.index('-s')
			if len(self.options) > i+1:
				return str(self.options[i+1]).lstrip('-s').split(',')
		return []
