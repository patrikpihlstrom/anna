#!/usr/bin/env python

import argparse

from . import anna
from . import test_manager

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='End-to-end testing using selenium')
	parser.add_argument('-d', '--drivers', nargs='+', required=True, help='Names of the drivers (separate by space).')
	parser.add_argument('-s', '--sites', nargs='+', required=True, help='Names of the sites to test (separate by space).')
	parser.add_argument('-v', '--verbose', action='store_true', help='Print exceptions and stack traces while running.')
	parser.add_argument('-H', '--headless', action='store_true', help='Run drivers in headless mode.')
	parser.add_argument('-r', '--resolution', required=False, help='Set the driver resolution (defaults to 1920x1080).')
	parser.add_argument('-i', '--id', required=False, help='Set the id (used by anna-api).')
	args = vars(parser.parse_args())
	bot = anna.Anna(args)
	bot.set_tests(test_manager.get_tests(args['sites']))
	bot.run()
