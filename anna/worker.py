import driver.factory


class Worker:
	def __init__(self, options):
		self.driver = None
		self.exceptions = []
		self.options = options

	def close(self):
		self.driver.close()

	def run(self, url, tasks):
		self.driver = driver.factory.create(self.options)
		self.driver.get(url)
		for task in tasks:
			task.run(self.driver, self.options)
