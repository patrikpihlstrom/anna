from src.util import get_element


def current_url(driver, url):
    return {'key': 'current_url', 'pass': driver.current_url == url}


def element_exists(driver, target):
    return {'key': 'element_exists', 'pass': get_element(driver, target) is not None}
