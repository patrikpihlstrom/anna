# anna
**End-to-end website testing software using selenium**

### Usage
I've made docker containers for [firefox](https://github.com/patrikpihlstrom/docker-anna-firefox) & [chrome](https://github.com/patrikpihlstrom/docker-anna-chrome).

Run ```anna```

| arg | description             |required|
|-----|-------------------------|---------------|
| -d  | specify the drivers (seperate by space)|yes|
| -s  | specify the sites (seperate by space)|yes|
| -h  | display help|no|
| -v  | verbose mode|no|
| -H  | run in headless mode|no|
| -r  | specify the resolution of the drivers (defaults to 1920x1080)|no|

### Test definitions
Test cases are defined in the ```tests/anna/``` directory. Each website should have
a json file as well as a subdirectory under ```tests/anna/``` containing test definitions.
If a test is referenced, but not defined for a particular website,
anna will use the ```base``` directory as a fallback.
Consider the following file structure:
```
anna/
    tests/
    	anna/
		example.json
		base/
			do_thing.json
		example/
			go_to_page.json
```

Example website configuration (```tests/anna/example.json```):
```
{
  "url": "https://example.com",
  "sequence": {
    "0": "do_thing",
    "1": "go_to_page"
  }
}
```
Example test definition (```tests/anna/example/go_to_page.json```):
```
{
  "events": [
    {
      "type": "click",
      "target": ".target-class"
    },
    ...
  ],
  "expected_result": {
    "current_url": "https://example.com/page/"
  }
}
```

### Currently implemented event types
* click ```{"type": "click", "target": "#unique_element}```
* sendkeys ```{"type": "sendkeys", "target": "#unique_element}```
* submit ```{"type": "submit", "target": "#unique_element}```
* hover ```{"type": "hover", "target": "#unique_element}```
* wait ```{"type": "wait", "target": "#unique_element}```

### Currently implemented assertion types
* current_url ```{"current_url": "https://example.com/somepage"}```
* element_exists ```{"element_exists": ".some-class"}```

#### TODO
* Change test assertion definition structure
* Implement built-in wait in assertions
* Implement database assertions
* Implement subroutine processing
