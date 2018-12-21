from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from src.util import get_element
import time


def sendkeys(driver, event):
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
    action = ActionChains(driver).move_to_element(element)
    action.perform()


def get(driver, event):
    driver.get(event['target'])


def wait(driver, event):
    try:
        if 'id' in event['target']:
            WebDriverWait(driver, 16).until(ec.presence_of_element_located((By.ID, event['target']['id'])))
            return True
        if 'class' in event['target']:
            WebDriverWait(driver, 16).until(ec.presence_of_element_located((By.CLASS_NAME, event['target']['class'])))
            return True
        if 'href' in event['target']:
            WebDriverWait(driver, 16).until(ec.presence_of_element_located((By.LINK_TEXT, event['target']['href'])))
            return True
    except TimeoutException:
        pass

    return False


def sleep(driver, event):
    time.sleep(event['value'])

