import sys
import time
import traceback

import colors
import driver
import events
import result

import selenium.common.exceptions


class Anna:
	def __init__(self, options):
		self.driver = None
		self.tests = {}
		self.exceptions = []
		self.options = options
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
			result = test.assert_result(self.driver)
			if not any(not assertion['pass'] for assertion in result['assertions']):
				print(colors.green + 'passed' + colors.white)
			else:
				raise Exception
			self.screenshot(test)
			self.result.append(result)
		except Exception as e:  # log any and all exceptions that occur during tests
			self.screenshot(test)
			print(colors.red + 'failed' + colors.white)
			self.result.record_exception(e, test, event, self.options, self.driver)
			if self.options['verbose']:
				traceback.print_exc(file=sys.stdout)
			pass

	def run(self):
		"""
		Run all tests in all browsers on all sites
		:return:
		"""
		for d in self.options['drivers']:
			for site in self.tests.keys():
				self.driver = driver.get_driver(d, self.options)
				self.driver.get(site)
				for test in self.tests[site]:
					self.run_test(test)
				self.close()
		self.result.print_results(self.options)
		return self.result

	def screenshot(self, test):
		"""
		Attempts to save a screenshot of the current driver
		"""
		if 'id' in self.options and type('id') is not None:
			try:
				path = '/tmp/' + '_'.join((str(self.options['id']), test.site, self.driver.name, test.name)) + '.png'
				self.driver.save_screenshot(path)
				return path
			except selenium.common.exceptions.WebDriverException:
				return False
		return False

	def set_tests(self, tests):
		self.tests = tests
