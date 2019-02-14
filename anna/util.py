import time


def get_element(driver, target, return_list=False, timeout=16):
    time.sleep(1)
    try:
        element = driver.find_element_by_css_selector(target)
    except:
        element = None

    # default behavior is to return the first element that matches
    if type(element) is list:
        if len(element) == 0:
            if timeout <= 0:
                return False
            return get_element(driver, target, return_list, timeout - 1)
        if not return_list:
            return element[0]
    elif element is None:
        if timeout <= 0:
            return False
        return get_element(driver, target, return_list, timeout - 1)
    return element
