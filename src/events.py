import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

from src.util import get_element


def send_keys(driver, event):
	wait(driver, event)
	element = get_element(driver, event['target'])
	v = event['value'].encode('ascii', 'ignore').decode("utf-8")
	element.send_keys(v)


def submit(driver, event):
	wait(driver, event)
	element = get_element(driver, event['target'])
	element.submit()


def click(driver, event):
	wait(driver, event)
	element = get_element(driver, event['target'])
	element.click()


def hover(driver, event):
	wait(driver, event)
	element = get_element(driver, event['target'])
	action = ActionChains(driver)
	action.move_to_element(element)
	action.perform()


def get(driver, event):
	driver.get(event['target'])


def wait(driver, event):
	"""
	Wait for an element to appear
	:param driver:
	:param event:
	:return:
	"""
	if 'id' in event['target']:
		if event['type'] == 'click':
			WebDriverWait(driver, 16).until(ec.element_to_be_clickable((By.ID, event['target']['id'])))
		else:
			WebDriverWait(driver, 16).until(ec.presence_of_element_located((By.ID, event['target']['id'])))
		return True
	if 'class' in event['target']:
		if event['type'] == 'click':
			WebDriverWait(driver, 16).until(ec.element_to_be_clickable((By.CLASS_NAME, event['target']['class'])))
		else:
			WebDriverWait(driver, 16).until(ec.presence_of_element_located((By.CLASS_NAME, event['target']['class'])))
		return True
	if 'href' in event['target']: # selenium.webdriver.common.by doesn't support href selection
		slept = 0
		while slept < 16:
			element = get_element(driver, event['target'])
			if element is not None:
				break
			time.sleep(1)
			slept += 1
		return True

	return False


def sleep(driver, event):
	time.sleep(event['value'])


def switch_to(driver, event):
	driver.switch_to.frame(get_element(driver, event['target']))