from src.assertions import *


class Test:
    def __init__(self, name, order, events, expected_result, url):
        self.name = name
        self.order = order
        self.events = events
        self.expected_result = expected_result
        self.url = url

    def assert_result(self, driver):
        result = {'name': self.name, 'driver': driver.name, 'assertions': []}
        for key, val in self.expected_result.items():
            if key == 'current_url':
                val = val.encode('ascii', 'ignore').decode("utf-8")
                result['assertions'].append(current_url(driver, val))
            elif key == 'element_exists':
                result['assertions'].append(element_exists(driver, val))
        return result
