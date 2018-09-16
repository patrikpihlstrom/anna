class Test:
    def __init__(self, name, order, events, expected_result):
        self.name = name
        self.order = order
        self.events = events
        self.expected_result = expected_result

    def assert_result(self, driver):
        result = {'name': self.name, 'driver': driver.name, 'assertions': []}
        for key, val in self.expected_result.items():
            val = val.encode('ascii', 'ignore').decode("utf-8")
            if key == 'current_url':
                result['assertions'].append({'key': key, 'pass': driver.current_url == val})
        return result
