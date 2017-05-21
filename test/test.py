#!/usr/bin/python

import unittest
import json

from magento_bot import magento_bot


class TestMagentoBot(unittest.TestCase):
    config = None
    test = None

    def __init__(self, test, config):
        super(TestMagentoBot, self).__init__('test_'+test['function'])
        self.test = test
        self.config = config

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_add_to_cart(self):
        bot = magento_bot.MagentoBot(self.config)
        bot.open()
        bot.close()

if __name__ == '__main__':
    config = None
    with open('./config.json') as config:
        config = json.load(config)

    for driver in config['drivers']:
        suite = unittest.TestSuite()
        config['driver'] = driver
        for test in config['tests']:
            suite.addTest(TestMagentoBot(test, config))

        unittest.TextTestRunner().run(suite)

