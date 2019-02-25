import sys
import traceback
from pprint import pprint

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
			if not self.execute_task(task):
				break
		self.print_result()

	def execute_task(self, task):
		print('Running %s @ %s on %s' % (task.name, task.url, self.driver.name))
		try:
			task.execute_events(self.driver, events)
			task.check(self.driver, assertions)
		except KeyboardInterrupt:
			return False
		except:  # log any and all exceptions that occur during tasks
			task.passed = False
			task.result = traceback.format_exc()
			assert len(task.event) > 0
			if self.options['verbose']:
				traceback.print_exc(file=sys.stdout)
		if task.passed:
			print(colors.green + 'passed' + colors.white)
		else:
			print(colors.red + 'failed' + colors.white)
		return True

	def print_result(self):
		if self.options['verbose']:
			self.print_task_summary()
		passed = len([task for task in self.tasks if task.passed])
		print(str(passed) + '/' + str(len(self.tasks)))

	def print_task_summary(self):
		for task in self.tasks:
			if task.passed:
				print(colors.green)
				pprint(task.dict())
			else:
				print(colors.red)
				pprint(task.dict())
			print(colors.white)
