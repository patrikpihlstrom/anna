#!/usr/bin/python

import sys
import unittest

loader = unittest.TestLoader()
driver = ''
if len(sys.argv) > 1:
	driver = sys.argv[1]

if driver not in ('chrome', 'firefox'):
	suite = loader.discover('tests/unit')
else:
	suite = loader.discover('tests/unit/' + driver)

print(driver)
print('found ' + str(suite.countTestCases()) + ' test cases')
unittest.TextTestRunner().run(suite)
