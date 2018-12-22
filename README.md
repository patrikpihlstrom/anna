# mage-bot
**website testing software using selenium**
## Configuration definition
Configuration values for drivers and database credentials **(TODO)** are defined in ```config.json``` and should conform to the following format:
```
{
  "drivers": [
    "firefox",
    "chrome"
  ]
}
```
## Test definitions
Tests are defined in the ```tests/``` directory. Each website should have
a json file as well as a subdirectory under ```tests/``` containing test definitions.
If a test is referenced, but not defined for a particular website,
mage-bot will use the ```base``` directory as a fallback.
Consider the following file structure:
```
mage-bot/
    tests/
        example.json
        base/
            do_thing.json
        example/
            go_to_page.json
```

Example website configuration (```tests/example.json```):
```
{
  "url": "https://example.com",
  "sequence": {
    "0": "do_thing",
    "1": "go_to_page"
  }
}
```
Example test definition (```tests/example/go_to_page.json```):
```
{
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
    "current_url": "https://example.com/page/"
  }
}
```

### Currently implemented event types
* click ```{"type": "click", "target": {"id": "unique_element}```
* sendkeys ```{"type": "sendkeys", "target": {"id": "unique_element}```
* submit ```{"type": "submit", "target": {"id": "unique_element}```
* hover ```{"type": "hover", "target": {"id": "unique_element}```
* wait ```{"type": "wait", "target": {"id": "unique_element}```

### Currently implemented target selectors
* id ```{"target": {"id": "unique_element"}}```
* class ```{"target": {"class": "some-class"}}```
* href ```{"target": {"href": "https://example.com/somepage"}}```

### Currently implemented assertion types
* current_url ```{"current_url": "https://example.com/somepage"}```
* element_exists ```{"element_exists": {"class": "some-class"}}```

#### TODO
* Change test assertion definition structure
* Implement built-in wait in assertions
* Implement database assertions
* Implement subroutine processing
