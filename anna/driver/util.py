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
	time.sleep(1)
	if get_first:
		try:
			element = driver.find_element_by_css_selector(target)
		except:
			element = None
		if element is None:
			if timeout <= 0:
				return False
			return get_element(driver, target, get_first, timeout - 1)
		return element
	else:
		try:
			element = driver.find_elements_by_css_selector(target)
		except:
			element = []
		if not element:
			if timeout <= 0:
				return []
			return get_element(driver, target, get_first, timeout - 1)
		return element


def get_text(driver, target):
	element = get_element(driver, target, True)
	return element.text
