import sys, imp, traceback, string
from pprint import pprint

import anna.colors as colors
from anna_lib.selenium import factory


class Worker:
	def __init__(self, options):
		self.tasks = []
		self.driver = None
		self.options = options

	def close(self):
		self.driver.close()

	def run(self, url, tasks):
		self.driver = factory.create(self.options)
		self.driver.get(url)
		for task in tasks:
			module = imp.new_module(task[0])
			exec(task[1], module.__dict__)
			task_class = string.capwords(task[0].split('.')[-1].replace('_', ' ')).replace(' ', '')
			task = module.__dict__[task_class](self.driver)
			self.execute_task(url, module.__dict__['__name__'], task)
			self.tasks.append(task)

		self.print_result()

	def execute_task(self, url, name, task):
		print('Running %s @ %s on %s' % (name, url, self.driver.name))
		try:
			task.before_execute()
			task.execute()
			task.after_execute()
		except KeyboardInterrupt:
			return False
		except:  # log any and all exceptions that occur during tasks
			task.passed = False
			task.result = traceback.format_exc()
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
				pprint(task.result)
			else:
				print(colors.red)
				pprint(task.result)
			print(colors.white)
