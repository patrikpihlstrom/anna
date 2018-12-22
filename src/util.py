import src.events as events

def get_element(driver, target, return_list=False):
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
	# default behavior is to return the first element that matches
	if type(element) is list:
		if len(element) == 0:
			return None
		if not return_list:
			return element[0]
	return element
