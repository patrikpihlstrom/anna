import unittest

from selenium import common

from anna.driver import factory as driver_factory
from anna.driver import assertions, events
from anna.task import factory as task_factory


class TestAssertions(unittest.TestCase):
	def setUp(self):
		self.driver = driver_factory.create({'driver': 'chrome', 'headless': True})
		self.driver.get('http://annahub.se:8000/test/')
		self.assertEqual(self.driver.name, 'chrome')
		self.targets = {'#test-click': True, '#test-submit': True, '#not-found': False,
		                'a[href^="http://annahub.se:8000/test/switchto"]': True,
		                'a[href="http://annahub.se:8000/test"]': False}

	def tearDown(self):
		self.driver.close()

	def test_current_url_in(self):
		url = task_factory.get_url('test')
		self.driver.get(url)
		task = task_factory.create('current_url', 'test', url)
		task.execute_events(self.driver, events)
		self.assertTrue(assertions.current_url_in(self.driver, 'test/switchto')['pass'])
		self.assertFalse(assertions.current_url_in(self.driver, 'test/false')['pass'])

	def test_current_url_is(self):
		url = task_factory.get_url('test')
		self.driver.get(url)
		task = task_factory.create('current_url', 'test', url)
		task.execute_events(self.driver, events)
		self.assertTrue(assertions.current_url_is(self.driver, 'http://annahub.se:8000/test/switchto')['pass'])
		self.assertFalse(assertions.current_url_is(self.driver, 'test/switchto')['pass'])

	def test_element_exists(self):
		for target, result in self.targets.items():
			try:
				self.assertEqual(result, assertions.element_exists(self.driver, {'target': target})['pass'])
			except common.exceptions.NoSuchElementException as e:
				if not result:
					pass
				else:
					raise common.exceptions.NoSuchElementException(e)
