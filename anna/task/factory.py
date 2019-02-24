import os
import json

from . import task


def get_url(site):
	path = os.path.dirname(__file__) + '/../../tasks/'
	for file in [file for file in os.listdir(path) if file.endswith('.json')]:
		site_name = os.path.splitext(file)[0]
		if site_name in site:
			with open(path + file) as site_tasks:
				site_tasks = json.load(site_tasks)
				assert 'url' in site_tasks
				return site_tasks['url']


def open_task_definition(site, task):
	pass


def get_tasks(site):
	"""
	Parses the contents of JSON files in "tasks/" & continues to parse the task definitions in each of the files'
	corresponding sub-directory via the get_task function
	"""
	tasks = []
	path = os.path.dirname(__file__) + '/../../tasks/'
	for file in [file for file in os.listdir(path) if file.endswith('.json')]:
		site_name = os.path.splitext(file)[0]
		if site_name in site:
			with open(path + file) as site_tasks:
				site_tasks = json.load(site_tasks)
				url = site_tasks['url']
				sequence = site_tasks['sequence']
				for i in sequence:
					task = create(sequence[i], site_name, site_tasks['url'])
					if task is not False:
						tasks.append(task)
				return url, tasks


def create(name, site, url):
	"""
	Parses site-specific task definitions
	"""
	path = os.path.dirname(__file__) + '/../../tasks/'
	# check if the file exists in the site scope
	if os.path.isfile(path + site + '/' + name + '.json'):
		file = path + site + '/' + name + '.json'
	elif os.path.isfile(path + 'base/' + name + '.json'):  # fallback
		file = path + 'base/' + name + '.json'
	else:
		return False

	with open(file) as file:
		task = json.load(file)
		return task.Task(name, task['events'], task['assertions'], url, site)
