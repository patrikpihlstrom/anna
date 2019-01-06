from assertions import *


class Test:
    def __init__(self, name, events, expected_result, url):
        self.name = name
        self.events = events
        self.expected_result = expected_result
        self.url = url

    def assert_result(self, driver):
        result = {'name': self.name, 'url': self.url, 'driver': driver.name, 'assertions': []}
        for key, val in self.expected_result.items():
            if key == 'current_url':
                result['assertions'].append(current_url(driver, val))
            elif key == 'element_exists':
                result['assertions'].append(element_exists(driver, val))
        return result
