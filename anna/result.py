import colors


class Result:
	results = []
	exceptions = []

	def print_results(self, options):
		"""
		Get the ratio & display the results
		:param options:
		:return:
		"""
		failed = 0
		for result in self.results:
			if any(not assertion['pass'] for assertion in result['assertions']):
				if options['verbose']:
					print(colors.red + str(result) + colors.white)
				failed += 1
			elif options['verbose']:
				print(colors.green + str(result) + colors.white)
		if len(self.results) > 0:
			ratio = float(failed) / float(len(self.results))
		else:
			ratio = 1
		if failed == 0:  # all tests passed
			print(colors.green + '%x/%x tests passed' % (len(self.results) - failed, len(self.results)) + colors.white)
		elif ratio >= 0.33:  # less than 1/3 of the tests passed
			print(colors.red + '%x/%x tests passed' % (len(self.results) - failed, len(self.results)) + colors.white)
		else:
			print(colors.yellow + '%x/%x tests passed' % (len(self.results) - failed, len(self.results)) + colors.white)

	def record_exception(self, e, test, event, options, driver):
		"""
		Print the exception if we're in verbose mode, and then store it
		:param e:
		:param test:
		:param event:
		:param options:
		:param driver:
		:return:
		"""
		exception = {
			'test': test.name,
			'url': test.url,
			'driver': driver.name,
			'event': event,
			'exception': repr(e),
			'assertions': [{'pass': False}]
		}
		if '-v' in options:
			print(colors.red + str(exception) + colors.white)
		self.exceptions.append(exception)
		self.results.append(exception)

	def append(self, result):
		self.results.append(result)
