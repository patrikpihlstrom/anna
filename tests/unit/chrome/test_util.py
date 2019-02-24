import unittest

from anna.driver import factory
from anna.driver import util


class TestUtil(unittest.TestCase):
	def setUp(self):
		self.driver = factory.create({'driver': 'chrome', 'headless': True})
		self.targets = ['#test-send-keys']
		self.driver.get('http://annahub.se:8000/test/')
		self.assertEqual(self.driver.name, 'chrome')

	def tearDown(self):
		self.driver.close()

	def test_get_element_get_first(self):
		self.assertFalse(util.get_element(self.driver, '.not-found', 0))
		for target in self.targets:
			self.assertNotEqual(False, util.get_element(self.driver, target, 0))

	def test_get_element_get_list(self):
		self.assertEqual([], util.get_element(driver=self.driver, target='.not-found', get_first=False, timeout=0))
		self.assertIsInstance(util.get_element(driver=self.driver, target='.get-list', get_first=False, timeout=0), list)
		self.assertEqual(10, len(util.get_element(driver=self.driver, target='.get-list', get_first=False, timeout=0)))
