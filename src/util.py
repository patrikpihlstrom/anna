import time


def get_element(driver, target, return_list=False, timeout=16):
	element = None
	if 'id' in target:
		element = driver.find_element_by_id(target['id'])
	elif 'class' in target:
		element = driver.find_elements_by_class_name(target['class'])
	elif 'href' in target:
		element = driver.find_element_by_xpath("//a[@href='" + target['href'] + "']")
	elif 'data' in target:
		element = driver.find_element_by_xpath(
			"//[@" + target['data']['key'] + "='" + target['data']['value'] + "']")
	elif 'css' in target:
		element = driver.find_element_by_css_selector(target['css'])
	# default behavior is to return the first element that matches
	if type(element) is list:
		if len(element) == 0:
			if timeout <= 0:
				return False
			time.sleep(1)
			return get_element(driver, target, return_list, timeout - 1)
		if not return_list:
			return element[0]
	elif element is None:
		if timeout <= 0:
			return False
		time.sleep(1)
		return get_element(driver, target, return_list, timeout - 1)
	return element
