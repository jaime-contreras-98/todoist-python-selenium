import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException


class Helpers(object):

    def __init__(self, driver):
        self.driver = driver

    def element_is_present(self, locator):
        try:
            element = EC.presence_of_element_located(locator)
            WebDriverWait(self.driver, 10).until(element)
            assert True
        except NoSuchElementException:
            print('Element does not exist!')
            assert False

    def element_contains_partial_text(self, locator, text):
        try:
            element_text = EC.text_to_be_present_in_element(locator, text)
            WebDriverWait(self.driver, 10).until(element_text)
            assert True
        except WebDriverException:
            print('Element text does not match ', text)
            assert False

    def element_contains_text(self, locator, text):
        try:
            element_text = EC.text_to_be_present_in_element(locator, text)
            WebDriverWait(self.driver, 10).until(element_text)
            assert True
        except WebDriverException:
            print('Element text does not match ', text)
            assert False

    def click_visible_element(self, locator):
        try:
            element_visible = EC.element_to_be_clickable(locator)
            WebDriverWait(self.driver, 10).until(element_visible)
            self.driver.find_element(*locator).click()
            assert True
        except NoSuchElementException:
            print('Element does not exist, cannot be clicked!')
            assert False

    def find_dynamic_element_click(self, selector, text):
        my_selector = selector

        if "TEXT" in my_selector:
            new_word = my_selector.replace("TEXT", text)
            new_selector = self.driver.find_element(By.CSS_SELECTOR, new_word)
            new_selector.click()
            # time.sleep(1)
            assert True
        else:
            print("Not a valid selector")
            assert False

    def wait_seconds(self, seconds):
        time.sleep(int(seconds))

    # NO SIRVE
    def hover_on_element(self, selector):
        hover_element = self.driver.find_element(selector)
        hover = ActionChains(self.driver).move_to_element(hover_element)
        hover.perform()
