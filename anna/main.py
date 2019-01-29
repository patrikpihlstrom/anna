#!/usr/bin/env python

from sys import argv

import anna
import test_manager

if __name__ == '__main__':
	bot = anna.Anna()
	for arg in argv:
		bot.set_option(arg)
	bot.set_tests(test_manager.get_tests(bot.get_sites()))
	bot.run()
