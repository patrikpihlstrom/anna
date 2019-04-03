from selenium import common
import unittest

from anna.driver import assertions, events, factory as driver_factory
from anna_common.task import Task


class TestEvents(unittest.TestCase):
	driver = None
	options = {'driver': 'firefox', 'headless': False, 'verbose': False, 'sites': ['test']}

	def setUp(self):
		self.driver = driver_factory.create(self.options)

	def tearDown(self):
		self.driver.close()

	def test_click(self):
		self.driver.get('http://annahub.se:8000/test/')
		task = Task().load_from_test_module('click')
		task.execute_events(self.driver, events)
		self.assertTrue(task.check(self.driver, assertions))

	def test_current_url(self):
		self.driver.get('http://annahub.se:8000/test/')
		task = Task().load_from_test_module('current_url')
		task.execute_events(self.driver, events)
		self.assertTrue(task.check(self.driver, assertions))

	def test_send_keys(self):
		self.driver.get('http://annahub.se:8000/test/')
		task = Task().load_from_test_module('send_keys')
		task.execute_events(self.driver, events)
		self.assertTrue(task.check(self.driver, assertions))

	def test_submit(self):
		self.driver.get('http://annahub.se:8000/test/')
		task = Task().load_from_test_module('submit')
		task.execute_events(self.driver, events)
		self.assertTrue(task.check(self.driver, assertions))

	def test_switch_to(self):
		self.driver.get('http://annahub.se:8000/test/')
		task = Task().load_from_test_module('switch_to')
		task.execute_events(self.driver, events)
		self.assertTrue(task.check(self.driver, assertions))

	def test_hover(self):
		self.driver.get('http://annahub.se:8000/test/')
		task = Task().load_from_test_module('hover')
		task.execute_events(self.driver, events)
		self.assertTrue(task.check(self.driver, assertions))

	def test_wait(self):
		self.driver.get('http://annahub.se:8000/test/')
		task = Task().load_from_test_module('wait')
		task.execute_events(self.driver, events)
		self.assertTrue(task.check(self.driver, assertions))

	def test_fail(self):
		self.driver.get('http://annahub.se:8000/test/')
		task = Task().load_from_test_module('fail')
		try:
			task.execute_events(self.driver, events)
			result = task.check(self.driver, assertions)
			self.assertFalse(result)
		except common.exceptions.NoSuchElementException:
			pass

	def test_iframe_click(self):
		self.test_switch_to()
		task = Task().load_from_test_module('iframe.click')
		task.execute_events(self.driver, events)
		self.assertTrue(task.check(self.driver, assertions))

	def test_iframe_send_keys(self):
		self.test_switch_to()
		task = Task().load_from_test_module('iframe.send_keys')
		task.execute_events(self.driver, events)
		self.assertTrue(task.check(self.driver, assertions))

	def test_iframe_submit(self):
		self.test_switch_to()
		task = Task().load_from_test_module('iframe.submit')
		task.execute_events(self.driver, events)
		self.assertTrue(task.check(self.driver, assertions))

	def test_iframe_hover(self):
		self.test_switch_to()
		task = Task().load_from_test_module('iframe.hover')
		task.execute_events(self.driver, events)
		self.assertTrue(task.check(self.driver, assertions))

	def test_iframe_wait(self):
		self.test_switch_to()
		task = Task().load_from_test_module('iframe.wait')
		task.execute_events(self.driver, events)
		self.assertTrue(task.check(self.driver, assertions))

	def test_required_event(self):
		task = Task().load_from_test_module('required.true')
		with self.assertRaises(common.exceptions.TimeoutException):
			task.execute_events(self.driver, events)
		task = Task().load_from_test_module('required.false')
		task.execute_events(self.driver, events)
