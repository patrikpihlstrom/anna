from selenium import webdriver


def get_driver(name, options=[]):
	"""
	Returns a new webdriver by the requested name
	pass -h to run in headless mode
	"""
	if name == 'chrome':
		o = webdriver.ChromeOptions()
		o.headless = '-h' not in options
		return webdriver.Chrome(options=o)
	elif name == 'firefox':
		o = webdriver.FirefoxOptions()
		o.headless = '-h' not in options
		return webdriver.Firefox(options=o)
	elif name == 'ie':
		o = webdriver.IeOptions()
		o.headless = '-h' not in options
		return webdriver.Ie(options=o)
	elif name == 'edge':
		return webdriver.Edge()
	return False