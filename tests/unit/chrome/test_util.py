import unittest

from anna.driver import factory
from anna.driver import util


class TestUtil(unittest.TestCase):
	driver = factory.create({'driver': 'chrome', 'headless': True})

	def setUp(self):
		self.targets = (
			{'type': 'css', 'value': '#test-send-keys'},
			{'type': 'xpath', 'value': '//select[@name="xpath"]/option[@value="option"]'}
		)
		self.list_targets = (
			{'type': 'css', 'value': '.not-found'},
			{'type': 'css', 'value': '.get-list'}
		)
		self.driver.get('http://annahub.se:8000/test/')
		self.assertEqual(self.driver.name, 'chrome')

	def tearDown(self):
		self.driver.close()

	def test_get_element_get_first(self):
		self.assertFalse(
			util.get_element(driver=self.driver, target=self.list_targets[0]['value'], get_first=True, timeout=0))
		for target in self.targets:
			self.assertNotEqual(False, util.get_element(driver=self.driver, target=target['value'], get_first=True,
			                                            type=target['type']))

	def test_get_element_get_list(self):
		self.assertEqual([], util.get_element(driver=self.driver, target=self.list_targets[0]['value'], get_first=False,
		                                      timeout=0))
		self.assertIsInstance(
			util.get_element(driver=self.driver, target=self.list_targets[1]['value'], get_first=False, timeout=0),
			list)
		self.assertEqual(10, len(
			util.get_element(driver=self.driver, target=self.list_targets[1]['value'], get_first=False, timeout=0)))
