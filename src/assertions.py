from src.util import get_element
from src.events import wait


def current_url(driver, url):
    return {'key': 'current_url', 'pass': driver.current_url == url, 'current': driver.current_url, 'expected': url}


def element_exists(driver, target):
    wait(driver, {'target': target})
    return {'key': 'element_exists', 'pass': get_element(driver, target) is not None}
