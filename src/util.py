def get_element(driver, target):
    try:
        if 'id' in target:
            element = driver.find_element_by_id(target['id'])
        elif 'class' in target:
            element = driver.find_elements_by_class_name(target['class'])[0]
        elif 'href' in target:
            element = driver.find_element_by_xpath("//a[@href='" + target['href'] + "']")
    except:
        raise AttributeError('unable to get element: ' + str(target))
    return element