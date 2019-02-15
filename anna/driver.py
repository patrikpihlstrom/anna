from selenium import webdriver


def get_driver(name, options=[]):
	"""
	Returns a webdriver based on the -d arg
	pass -h to run in headless mode
	"""

	if name == 'chrome':
		o = webdriver.ChromeOptions()
	elif name == 'firefox':
		o = webdriver.FirefoxOptions()
	elif name == 'ie':
		o = webdriver.IeOptions()
	elif name == 'edge':
		return webdriver.Edge()
	else:
		o = webdriver.ChromeOptions()
	o.headless = options['headless']

	if name == 'chrome':
		driver = webdriver.Chrome(options=o)
	elif name == 'firefox':
		driver = webdriver.Firefox(options=o)
	elif name == 'ie':
		driver = webdriver.Ie(options=o)
	else:
		driver = webdriver.Chrome(options)

	resolution = str(options['resolution']).split('x') if options['resolution'] is not None else (1920, 1080)
	driver.set_window_size(resolution[0], resolution[1])

	return driver
