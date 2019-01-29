import unittest

import config

from anna import driver, util, events


class TestEvents(unittest.TestCase):
    def setUp(self):
        self.actions = {
            'https://stage.lillynails.se.caupo.se/': {
                'send_keys': {'target': '#search', 'value': 'Gel Polish'},
                'submit': '',
                'click': '',
                'hover': '',
                'get': '',
                'wait': '',
                'switch_to': '',
            }
        }

    def test_send_keys(self):
        for d in config.drivers:
            d = driver.get_driver(d, [])
            for site, actions in self.actions.items():
                d.get(site)
                e = util.get_element(d, actions['send_keys']['target'])
                self.assertEqual(e.get_attribute('value'), '')
                events.send_keys(d, actions['send_keys'])
                e = util.get_element(d, actions['send_keys']['target'])
                self.assertEqual(e.get_attribute('value'), actions['send_keys']['value'])


if __name__ == '__main__':
    unittest.main()
