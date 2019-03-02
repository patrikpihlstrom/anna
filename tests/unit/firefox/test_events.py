from selenium import common
import unittest

from anna.driver import assertions, events, factory as driver_factory
from anna_common.task import Task


class TestEvents(unittest.TestCase):
	driver = None
	options = {'driver': 'firefox', 'headless': True, 'verbose': False, 'sites': ['test']}

	def setUp(self):
		self.driver = driver_factory.create(self.options)

	def tearDown(self):
		self.driver.close()

	def test_click(self):
		self.driver.get('http://annahub.se:8000/test/')
		for site in self.options['sites']:
			task = Task().load_from_module('click', site)
			task.execute_events(self.driver, events)
			self.assertTrue(task.check(self.driver, assertions))

	def test_current_url(self):
		self.driver.get('http://annahub.se:8000/test/')
		for site in self.options['sites']:
			task = Task().load_from_module('current_url', site)
			task.execute_events(self.driver, events)
			self.assertTrue(task.check(self.driver, assertions))

	def test_send_keys(self):
		self.driver.get('http://annahub.se:8000/test/')
		for site in self.options['sites']:
			task = Task().load_from_module('send_keys', site)
			task.execute_events(self.driver, events)
			self.assertTrue(task.check(self.driver, assertions))

	def test_submit(self):
		self.driver.get('http://annahub.se:8000/test/')
		for site in self.options['sites']:
			task = Task().load_from_module('submit', site)
			task.execute_events(self.driver, events)
			self.assertTrue(task.check(self.driver, assertions))

	def test_switch_to(self):
		self.driver.get('http://annahub.se:8000/test/')
		for site in self.options['sites']:
			task = Task().load_from_module('switch_to', site)
			task.execute_events(self.driver, events)
			self.assertTrue(task.check(self.driver, assertions))

	def test_hover(self):
		self.driver.get('http://annahub.se:8000/test/')
		for site in self.options['sites']:
			task = Task().load_from_module('hover', site)
			task.execute_events(self.driver, events)
			self.assertTrue(task.check(self.driver, assertions))

	def test_wait(self):
		self.driver.get('http://annahub.se:8000/test/')
		for site in self.options['sites']:
			task = Task().load_from_module('wait', site)
			task.execute_events(self.driver, events)
			self.assertTrue(task.check(self.driver, assertions))

	def test_fail(self):
		self.driver.get('http://annahub.se:8000/test/')
		for site in self.options['sites']:
			task = Task().load_from_module('fail', site)
			try:
				task.execute_events(self.driver, events)
				result = task.check(self.driver, assertions)
				self.assertFalse(result)
			except common.exceptions.NoSuchElementException:
				pass

	def test_iframe_click(self):
		self.test_switch_to()
		for site in self.options['sites']:
			task = Task().load_from_module('iframe/click', site)
			task.execute_events(self.driver, events)
			self.assertTrue(task.check(self.driver, assertions))

	def test_iframe_send_keys(self):
		self.test_switch_to()
		for site in self.options['sites']:
			task = Task().load_from_module('iframe/send_keys', site)
			task.execute_events(self.driver, events)
			self.assertTrue(task.check(self.driver, assertions))

	def test_iframe_submit(self):
		self.test_switch_to()
		for site in self.options['sites']:
			task = Task().load_from_module('iframe/submit', site)
			task.execute_events(self.driver, events)
			self.assertTrue(task.check(self.driver, assertions))

	def test_iframe_hover(self):
		self.test_switch_to()
		for site in self.options['sites']:
			task = Task().load_from_module('iframe/hover', site)
			task.execute_events(self.driver, events)
			self.assertTrue(task.check(self.driver, assertions))

	def test_iframe_wait(self):
		self.test_switch_to()
		for site in self.options['sites']:
			task = Task().load_from_module('iframe/wait', site)
			task.execute_events(self.driver, events)
			self.assertTrue(task.check(self.driver, assertions))
