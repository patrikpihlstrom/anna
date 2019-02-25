import sys
import traceback

import colors
from driver import factory, events, assertions


class Worker:
	def __init__(self, options):
		self.tasks = None
		self.driver = None
		self.exceptions = []
		self.options = options

	def close(self):
		self.driver.close()

	def run(self, url, tasks):
		self.tasks = tasks
		self.driver = factory.create(self.options)
		self.driver.get(url)
		for task in tasks:
			self.execute_task(task)
		self.print_result()

	def execute_task(self, task):
		print('Running %s @ %s on %s' % (task.name, task.url, self.driver.name))
		try:
			task.execute_events(self.driver, events)
			task.check(self.driver, assertions)
		except:  # log any and all exceptions that occur during tasks
			task.passed = False
			assert len(task.event) > 0
			if self.options['verbose']:
				traceback.print_exc(file=sys.stdout)
		if task.passed:
			print(colors.green + 'passed' + colors.white)
		else:
			print(colors.red + 'failed' + colors.white)

	def print_result(self):
		if self.options['verbose']:
			self.print_event_summary()
		passed = len([task for task in self.tasks if task.passed])
		print(str(passed) + '/' + str(len(self.tasks)))

	def print_event_summary(self):
		pass
