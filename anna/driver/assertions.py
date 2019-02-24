from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from anna.driver import util
import time


def current_url_in(driver, expected, timeout=16):
	passed = expected in driver.current_url
	if not passed and timeout > 0:
		time.sleep(1)
		return current_url_in(driver, expected, timeout - 1)
	return {'key': 'current_url', 'pass': passed, 'current': driver.current_url, 'expected': ['in', expected]}


def current_url_is(driver, expected, timeout=16):
	passed = driver.current_url == expected
	if not passed and timeout > 0:
		time.sleep(1)
		return current_url_is(driver, expected, timeout - 1)
	return {'key': 'current_url', 'pass': passed, 'current': driver.current_url, 'expected': expected}


def current_url(driver, assertion, timeout=16):
	if 'in' in assertion:
		return current_url_in(driver, assertion['in'], timeout)
	elif 'is' in assertion:
		return current_url_is(driver, assertion['is'], timeout)


def element_exists(driver, assertion, timeout=16):
	return {'key': 'element_exists',
	        'pass': util.get_element(driver, assertion['target'], timeout) not in [None, False, []]}


def clickable(driver, assertion, timeout=16):
	try:
		passed = WebDriverWait(driver, timeout).until(
			ec.element_to_be_clickable((By.CSS_SELECTOR, assertion['target']))) not in [None, False, []]
	except TimeoutException:
		passed = False
	return {'key': 'clickable', 'pass': passed}