import unittest

from anna.driver import factory as driver_factory
from anna.task import factory as task_factory


class TestEvents(unittest.TestCase):
	driver = None
	options = {'driver': 'firefox', 'headless': True, 'verbose': False, 'sites': ['test']}

	def setUp(self):
		self.driver = driver_factory.create(self.options)

	def tearDown(self):
		self.driver.close()

	def test_click(self):
		for site in self.options['sites']:
			url = task_factory.get_url(site)
			task = task_factory.create('click', site, url)
			self.driver.get(url)
			task.execute_events(self.driver)
			self.assertTrue(task.check(self.driver))

	def test_current_url(self):
		for site in self.options['sites']:
			url = task_factory.get_url(site)
			task = task_factory.create('current_url', site, url)
			self.driver.get(url)
			task.execute_events(self.driver)
			self.assertTrue(task.check(self.driver))

	def test_send_keys(self):
		for site in self.options['sites']:
			url = task_factory.get_url(site)
			task = task_factory.create('send_keys', site, url)
			self.driver.get(url)
			task.execute_events(self.driver)
			self.assertTrue(task.check(self.driver))

	def test_submit(self):
		for site in self.options['sites']:
			url = task_factory.get_url(site)
			task = task_factory.create('submit', site, url)
			self.driver.get(url)
			task.execute_events(self.driver)
			self.assertTrue(task.check(self.driver))

	def test_switch_to(self):
		for site in self.options['sites']:
			url = task_factory.get_url(site)
			task = task_factory.create('switch_to', site, url)
			self.driver.get(url)
			task.execute_events(self.driver)
			self.assertTrue(task.check(self.driver))

	def test_hover(self):
		for site in self.options['sites']:
			url = task_factory.get_url(site)
			task = task_factory.create('hover', site, url)
			self.driver.get(url)
			task.execute_events(self.driver)
			self.assertTrue(task.check(self.driver))

	def test_wait(self):
		for site in self.options['sites']:
			url = task_factory.get_url(site)
			task = task_factory.create('wait', site, url)
			self.driver.get(url)
			task.execute_events(self.driver)
			self.assertTrue(task.check(self.driver))

	def test_fail(self):
		for site in self.options['sites']:
			url = task_factory.get_url(site)
			task = task_factory.create('fail', site, url)
			self.driver.get(url)
			task.execute_events(self.driver)
			self.assertFalse(task.check(self.driver))

	def test_iframe_click(self):
		self.test_switch_to()
		for site in self.options['sites']:
			url = task_factory.get_url(site)
			task = task_factory.create('iframe/click', site, url)
			task.execute_events(self.driver)
			self.assertTrue(task.check(self.driver))

	def test_iframe_send_keys(self):
		self.test_switch_to()
		for site in self.options['sites']:
			url = task_factory.get_url(site)
			task = task_factory.create('iframe/send_keys', site, url)
			task.execute_events(self.driver)
			self.assertTrue(task.check(self.driver))

	def test_iframe_submit(self):
		self.test_switch_to()
		for site in self.options['sites']:
			url = task_factory.get_url(site)
			task = task_factory.create('iframe/submit', site, url)
			task.execute_events(self.driver)
			self.assertTrue(task.check(self.driver))

	def test_iframe_hover(self):
		self.test_switch_to()
		for site in self.options['sites']:
			url = task_factory.get_url(site)
			task = task_factory.create('iframe/hover', site, url)
			task.execute_events(self.driver)
			self.assertTrue(task.check(self.driver))

	def test_iframe_wait(self):
		self.test_switch_to()
		for site in self.options['sites']:
			url = task_factory.get_url(site)
			task = task_factory.create('iframe/wait', site, url)
			task.execute_events(self.driver)
			self.assertTrue(task.check(self.driver))
