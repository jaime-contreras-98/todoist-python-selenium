import unittest
from selenium import webdriver
from helpers.keywords import Helpers
from data.constants import Constants
from pom.locators.base_loc import BaseLoc
from pom.locators.home_loc import HomeLoc
from pom.locators.login_loc import LoginLoc
from pom.pages.login import Login


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(Constants.url[0])
        self.driver.find_element(*BaseLoc.signInLink).click()

    def test_login_positive(self):
        Login.login_form(self, Constants.r_username, Constants.r_password)
        Helpers.element_is_present(self, HomeLoc.headerLabel)

    def test_login_neg_bad_credentials(self):
        Login.login_form(self, Constants.f_username, Constants.f_password)
        Helpers.text_equal_to(self, LoginLoc.invErrorMsgLbl, Constants.error_msg[0])

    def test_login_neg_bad_email(self):
        Login.login_form(self, None, Constants.f_password)
        Helpers.text_equal_to(self, LoginLoc.emailErrorMsgLbl, Constants.error_msg[2])

    def test_login_neg_bad_password(self):
        Login.login_form(self, Constants.f_username, None)
        Helpers.text_equal_to(self, LoginLoc.passErrorMsgLbl, Constants.error_msg[1])

    def tearDown(self):
        self.driver.quit()

    if __name__ == "__main__":
        unittest.main()
