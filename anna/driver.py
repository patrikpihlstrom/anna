from selenium import webdriver


def get_driver(name, options=[]):
	"""
	Returns a new webdriver by the requested name
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

	o.headless = '-h' not in options
	if name == 'chrome':
		driver = webdriver.Chrome(options=o)
	elif name == 'firefox':
		driver = webdriver.Firefox(options=o)
	elif name == 'ie':
		driver = webdriver.Ie(options=o)
	else:
		driver = webdriver.Chrome(options=o)

	driver.set_window_size(1920, 1080)

	return driver
