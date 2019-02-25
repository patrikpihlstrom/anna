import time


def get_element(driver, target, get_first=True, timeout=16):
	"""
	Default behavior is to return the first element that matches the target
	:param driver:
	:param target:
	:param get_first:
	:param timeout:
	:return:
	"""
	try:
		if get_first:
			return driver.find_element_by_css_selector(target)
		else:
			return driver.find_elements_by_css_selector(target)
	except TimeoutError as e:
		if timeout <= 0:
			raise TimeoutError(e)
		time.sleep(1)
		return get_element(driver, target, get_first, timeout - 1)


def get_text(driver, target):
	element = get_element(driver, target, True)
	return element.text
