import assertions


class Test:
    def __init__(self, name, events, expected_result, url):
        self.name = name
        self.events = events
        self.expected_result = expected_result
        self.url = url

    def assert_result(self, driver):
        result = {'name': self.name, 'url': self.url, 'driver': driver.name, 'assertions': []}
        for key, val in self.expected_result.items():
            func = getattr(assertions, key)
            result['assertions'].append(func(driver, val))
        return result
