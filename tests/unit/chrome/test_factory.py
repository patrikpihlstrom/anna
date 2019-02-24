import unittest

from anna.driver import factory


class TestFactory(unittest.TestCase):
	def test_create(self):
		driver = factory.create({'driver': 'chrome', 'headless': True})
		self.assertEqual(driver.name, 'chrome')
		driver.close()
		driver = factory.create({'driver': 'chrome', 'headless': True, 'resolution': '640x480'})
		self.assertEqual(driver.name, 'chrome')
		size = driver.get_window_size()
		self.assertEqual('640x480', str(size['width']) + 'x' + str(size['height']))
		driver.close()
