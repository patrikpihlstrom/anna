# storobot
**Store testing software using selenium**
## Configuration definition
Configuration values for drivers and database credentials are defined in ```config.json``` and should conform to the following format:
```
{
  "drivers": [
    "firefox",
    "chrome"
  ],
  "base_url": "https://mystore.com/",
  "database": {
    "host": "host",
    "user": "user",
    "password": "password",
    "database": "mystore",
    "prefix": ""
  }
}
```
## Test definitions
Tests are defined in ```tests.json``` and should conform to the following format:
```
{
  "test_name": {
    "order": 0,
    "url": "https://mystore.com/",
    "events": [
      {
        "type": "click",
        "target": {
          "class": "target-class"
        }
      },
      ...
    ],
    "expected_result": {
      "current_url": "https://mystore.com/customer/account/"
    }
  }
}
```

### Currently implemented event types
* click ```{"type": "click", "target": {"id": "unique_element}```
* sendkeys ```{"type": "sendkeys", "target": {"id": "unique_element}```
* submit ```{"type": "submit", "target": {"id": "unique_element}```
* hover ```{"type": "hover", "target": {"id": "unique_element}```

### Currently implemented target selectors
* id ```{"target": {"id": "unique_element"}}```
* class ```{"target": {"class": "some-class"}}```
* href ```{"target": {"href": "https://mystore.com/somepage"}}```

### Currently implemented assertion types
* current_url ```{"current_url": "https://mystore.com/success"}```
* element_exists ```{"element_exists": {"class": "some-class"}}```
