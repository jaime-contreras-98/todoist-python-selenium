from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException


class Helpers(object):

    def element_is_present(self, locator):
        try:
            element = EC.presence_of_element_located(locator)
            WebDriverWait(self.driver, 8).until(element)
            assert True
        except TimeoutException:
            print('Element does not exist!')
            assert False

    def text_equal_to(self, locator, text):
        try:
            element_text = EC.text_to_be_present_in_element(locator, text)
            WebDriverWait(self.driver, 5).until(element_text)
            assert True
        except WebDriverException:
            print('Element text does not match ', text)
            assert False

    def click_visible_element(self, locator):
        try:
            element_visible = EC.element_to_be_clickable(locator)
            WebDriverWait(self.driver, 5).until(element_visible)
            self.driver.find_element(*locator).click()
            assert True
        except TimeoutException:
            print('Element does not exist, cannot be clicked!')
            assert False
