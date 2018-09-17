from selenium.webdriver import ActionChains

from src.util import get_element


def send_keys(driver, event):
    element = get_element(driver, event['target'])
    v = event['value'].encode('ascii', 'ignore').decode("utf-8")
    element.send_keys(v)


def submit(driver, event):
    element = get_element(driver, event['target'])
    element.submit()


def click(driver, event):
    element = get_element(driver, event['target'])
    element.click()


def hover(driver, event):
    element = get_element(driver, event['target'])
    action = ActionChains(driver).move_to_element(element)
    action.perform()
