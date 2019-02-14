import unittest

from . import options

from anna import driver, util
from selenium.common.exceptions import NoSuchElementException


class TestUtil(unittest.TestCase):
    def setUp(self):
        self.targets = {
            'http://127.0.0.1:8000/demo/': {
                '#send_keys': True,
                '#nonsense': False,
                '.btn-primary': True
            },
        }

    def test_get_element(self):
        for d in options.options['drivers']:
            d = driver.get_driver(d, options.options)
            for site, targets in self.targets.items():
                d.get(site)
                for target, expected_result in targets.items():
                    if expected_result:
                        self.assertTrue(util.get_element(d, target) not in (False, None, []))
                    else:
                        with self.assertRaises(NoSuchElementException):
                            util.get_element(d, target)
            d.close()


if __name__ == '__main__':
    unittest.main()
