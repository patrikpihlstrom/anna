import unittest

import config

from anna import driver, util
from selenium.common.exceptions import NoSuchElementException


class TestUtil(unittest.TestCase):
    def setUp(self):
        self.targets = {
            'https://stage.lillynails.se.caupo.se/': {
                '#search': True,
                '#nonsense': False,
                'a[href^="https://stage.lillynails.eu.caupo.se/"]': True
            },
            'https://google.com/': {
                '#searchform': True,
                '#bing': False,
                'form[action="/search"]': True
            }
        }

    def test_get_element(self):
        for d in config.drivers:
            d = driver.get_driver(d, [])
            for site, targets in self.targets.items():
                d.get(site)
                for target, expected_result in targets.items():
                    if expected_result:
                        self.assertTrue(util.get_element(d, target) not in (False, None, []))
                    else:
                        with self.assertRaises(NoSuchElementException):
                            util.get_element(d, target) not in (False, None, [])


if __name__ == '__main__':
    unittest.main()
