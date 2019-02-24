import sys
import traceback

import time
from selenium.common.exceptions import WebDriverException

from anna import colors
from driver import assertions
from driver import events


class Task:
	"""
	A task is a set of events that should execute in sequence. Once each event has been executed, the task will assert
	that the expected result was achieved. For instance, add_to_cart or place_order
	"""

	def __init__(self, name, events, assertions, url, site):
		self.name = name
		self.events = events
		self.assertions = assertions
		self.url = url
		self.site = site
		self.result = None
		self.passed = False
		self.exceptions = []

	def check(self, current_driver):
		result = {'test': self.name, 'url': self.url, 'driver': current_driver.name, 'assertions': []}
		for assertion in self.assertions:
			if hasattr(assertions, assertion['type']):
				func = getattr(assertions, assertion['type'])
				result['assertions'].append(func(current_driver, assertion))
		self.result = result
		self.passed = not any(not assertion['pass'] for assertion in self.result['assertions'])
		return self.passed

	def record_exception(self, exception, event, options, current_driver):
		exception = {
			'driver': current_driver.name,
			'event': event,
			'exception': repr(exception),
			'assertions': [{'pass': False}]
		}
		if '-v' in options:
			print(colors.red + str(exception) + colors.white)
		self.exceptions.append(exception)

	def screenshot(self, options, current_driver):
		"""
		Attempts to save a screenshot of the current driver
		"""
		if 'id' in options and type('id') is not None:
			try:
				path = '/tmp/' + '_'.join((str(options['id']), self.site, current_driver.name, self.name)) + '.png'
				current_driver.save_screenshot(path)
				return path
			except WebDriverException:
				return False
		return False

	def execute_events(self, current_driver):
		for event in self.events:
			time.sleep(1)
			if hasattr(events, event['type']):
				func = getattr(events, event['type'])
				func(current_driver, event)
				time.sleep(1)

	def run(self, current_driver, options={}):
		print('Running %s @ %s on %s' % (self.name, self.url, current_driver.name))
		event = None
		try:
			self.execute_events(current_driver)
			self.check(current_driver)
		except Exception as e:  # log any and all exceptions that occur during tasks
			self.passed = False
			self.record_exception(e, event, options, current_driver)
			if options['verbose']:
				traceback.print_exc(file=sys.stdout)
		if self.passed:
			print(colors.green + 'passed' + colors.white)
		else:
			print(colors.red + 'failed' + colors.white)
