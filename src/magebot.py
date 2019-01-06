#!/usr/bin/python

import time

import driver
import events


class Magebot:
	def __init__(self, config):
		self.config = None
		self.driver = None
		self.tests = {}
		self.exceptions = []
		self.options = []
		self.results = []
		self.config = config
		self.colors = ['\033[0m', '\033[92m', '\033[91m', '\033[93m']

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
			time.sleep(2)
			result = test.assert_result(self.driver)
			if not any(not assertion['pass'] for assertion in result['assertions']):
				print(self.colors[1] + 'passed' + self.colors[0])
			else:
				print(self.colors[2] + 'failed' + self.colors[0])
			self.results.append(result)
		except Exception as e:  # log any and all exceptions that occur during tests
			self.record_exception(e, test, event)
			pass

	def run(self):
		"""
		Run all tests in all browsers on all sites
		:return:
		"""
		for site in self.tests.keys():
			for driver_name in self.config['drivers']:
				self.driver = driver.get_driver(driver_name, self.options)
				self.driver.set_window_size(1920, 1080)
				self.driver.get(site)
				for test in self.tests[site]:
					self.run_test(test)
				self.close()
		self.print_results()

	def print_results(self):
		failed = 0
		for result in self.results:
			if any(not assertion['pass'] for assertion in result['assertions']):
				if '-v' in self.options:
					print(self.colors[2] + str(result) + self.colors[0])
				failed += 1
			elif '-v' in self.options:
				print(self.colors[1] + str(result) + self.colors[0])
		ratio = float(failed) / float(len(self.results))
		if failed == 0:
			print(self.colors[1] + '%x/%x tests passed' % (len(self.results) - failed, len(self.results)) + self.colors[0])
		elif ratio < 0.5:
			print(self.colors[2] + '%x/%x tests passed' % (len(self.results) - failed, len(self.results)) + self.colors[0])
		else:
			print(self.colors[3] + '%x/%x tests passed' % (len(self.results) - failed, len(self.results)) + self.colors[0])

	def set_tests(self, tests):
		self.tests = tests

	def set_option(self, arg):
		self.options.append(arg)

	def record_exception(self, e, test, event):
		exception = {
			'test': test.name,
			'url': test.url,
			'driver': self.driver.name,
			'event': event,
			'exception': repr(e)
		}
		if '-v' in self.options:
			print(self.colors[2] + str(exception))
		self.exceptions.append(exception)
