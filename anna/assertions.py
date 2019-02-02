import util
import time


def current_url(driver, url, timeout=16):
	if type(url) is dict:
		if 'in' in url:
			passed = url['in'] in driver.current_url
			if not passed and timeout > 0:
				time.sleep(1)
				return current_url(driver, url, timeout-1)
			return {'key': 'current_url', 'pass': passed, 'current': driver.current_url, 'expected': str(url)}
	else:
		passed = driver.current_url == url
		if not passed and timeout > 0:
			time.sleep(1)
			return current_url(driver, url, timeout-1)
		return {'key': 'current_url', 'pass': passed, 'current': driver.current_url, 'expected': url}


def element_exists(driver, target):
	return {'key': 'element_exists', 'pass': util.get_element(driver, target) not in [None, False, []]}
