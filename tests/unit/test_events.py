import unittest

from . import options

from anna import driver, util, events


class TestEvents(unittest.TestCase):
	def setUp(self):
		self.options = options.options
		self.url = 'http://127.0.0.1:8000/demo/'
		self.actions = {
			'send_keys': [{'target': '#send_keys', 'value': 'send_keys', 'type': 'send_keys'}],
			'submit': [{'target': '#submit', 'type': 'submit'}],
			'click': [{'target': '#click', 'type': 'click'}],
			'hover': [{'target': '#submit', 'type': 'hover'}],
			'get': [''],
			'wait': [''],
			'switch_to': [''],
		}

	def test_send_keys(self):
		for d in self.options['drivers']:
			d = driver.get_driver(d, self.options)
			d.get(self.url)
			for action in self.actions['send_keys']:
				e = util.get_element(d, action['target'])
				self.assertEqual('', e.get_attribute('value'))
				events.send_keys(d, action)
				e = util.get_element(d, action['target'])
				self.assertEqual(action['value'], e.get_attribute('value'))
			d.close()

	def test_click(self):
		for d in self.options['drivers']:
			d = driver.get_driver(d, self.options)
			d.get(self.url)
			for action in self.actions['click']:
				e = util.get_element(d, action['target'])
				self.assertEqual(None, e.get_attribute('checked'))
				events.click(d, action)
				e = util.get_element(d, action['target'])
				self.assertEqual('true', e.get_attribute('checked'))
			d.close()


if __name__ == '__main__':
	unittest.main()
