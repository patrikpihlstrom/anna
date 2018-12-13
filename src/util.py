def get_element(driver, target):
    element = None
    try:
        if 'id' in target:
            element = driver.find_element_by_id(target['id'])
        elif 'class' in target:
            element = driver.find_elements_by_class_name(target['class'])[0]
        elif 'href' in target:
            element = driver.find_element_by_xpath("//a[@href='" + target['href'] + "']")
        elif 'data' in target:
            element = driver.find_element_by_xpath(
                "//[@" + target['data']['key'] + "='" + target['data']['value'] + "']")
    except:
        return None
    return element
