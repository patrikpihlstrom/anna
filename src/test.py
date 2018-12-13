from src.assertions import *


class Test:
    def __init__(self, name, events, expected_result, url, site_configs):
        self.name = name
        self.events = events
        self.expected_result = expected_result
        self.url = url
        self.site_configs = site_configs

    def assert_result(self, driver):
        result = {'name': self.name, 'driver': driver.name, 'assertions': []}
        for key, val in self.expected_result.items():
            if key == 'current_url':
                val = val.encode('ascii', 'ignore').decode("utf-8")
                result['assertions'].append(current_url(driver, val))
            elif key == 'element_exists':
                result['assertions'].append(element_exists(driver, val))
        return result
