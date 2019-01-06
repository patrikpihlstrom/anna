from util import get_element


def current_url(driver, url):
	if type(url) is dict:
		if 'in' in url:
			return {'key': 'current_url', 'pass': url['in'] in driver.current_url, 'current': driver.current_url, 'expected': str(url)}
	return {'key': 'current_url', 'pass': driver.current_url == url, 'current': driver.current_url, 'expected': url}


def element_exists(driver, target):
	return {'key': 'element_exists', 'pass': get_element(driver, target) not in [None, False, []]}
