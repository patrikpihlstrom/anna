import time
from selenium.common.exceptions import WebDriverException


class Task:
	"""
	A task is a set of events that should execute in sequence. Once each event has been executed, the task will assert
	that the expected result was achieved. For instance, add_to_cart or place_order
	"""
	event: dict  # The event currently being executed

	def __init__(self, name, events, assertions, url, site):
		self.name = name
		self.events = events
		self.assertions = assertions
		self.url = url
		self.site = site
		self.result = None
		self.passed = False
		self.exceptions = []

	def check(self, current_driver, assertions):
		result = {'test': self.name, 'url': self.url, 'driver': current_driver.name, 'assertions': []}
		for assertion in self.assertions:
			if hasattr(assertions, assertion['type']):
				func = getattr(assertions, assertion['type'])
				result['assertions'].append(func(current_driver, assertion))
		self.result = result
		self.passed = not any(not assertion['pass'] for assertion in self.result['assertions'])
		return self.passed

	def screenshot(self, options, current_driver):
		"""
		Attempts to save a screenshot of the current driver
		"""
		if 'id' in options and type('id') in (int, str):
			try:
				path = '/tmp/' + '_'.join((str(options['id']), self.site, current_driver.name, self.name)) + '.png'
				current_driver.save_screenshot(path)
				return path
			except WebDriverException:
				return False
		return False

	def execute_events(self, current_driver, events):
		for event in self.events:
			self.event = event
			time.sleep(1)
			if hasattr(events, event['type']):
				func = getattr(events, event['type'])
				func(current_driver, event)
				time.sleep(1)
