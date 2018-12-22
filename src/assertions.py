from src.util import get_element
from src.events import wait


def current_url(driver, url):
	if type(url) is dict:
		if 'in' in url:
			return {'key': 'current_url', 'pass': driver.current_url in url, 'current': driver.current_url, 'expected': url}
	return {'key': 'current_url', 'pass': driver.current_url == url, 'current': driver.current_url, 'expected': url}


def element_exists(driver, target):
	return {'key': 'element_exists', 'pass': get_element(driver, target) is not None}
