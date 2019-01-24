#!/usr/bin/env python

import json
from sys import argv

from anna import Anna
from test_manager import get_tests

if __name__ == '__main__':
	with open('../config.json') as config:
		config = json.load(config)

	bot = Anna(config)
	for arg in argv:
		bot.set_option(arg)
	bot.set_tests(get_tests(bot.get_sites()))
	bot.run()
