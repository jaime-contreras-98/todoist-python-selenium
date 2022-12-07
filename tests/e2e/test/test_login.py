import unittest
from selenium import webdriver
from helpers.keywords import Helpers
from data.constants import Constants
from pom.locators.base_loc import BaseLoc
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pom.locators.sidebar_loc import SideBarLoc
from pom.locators.login_loc import LoginLoc
from pom.pages.login import Login


class LoginTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.headless = True
        print("========== LOGIN TESTS ==========")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.maximize_window()
        self.driver.get(Constants.url["prod"])
        self.driver.find_element(*BaseLoc.sign_in_lnk).click()

    def test_login_positive(self):
        Login.login_form(self, Constants.credentials["users"]["real"]["user"], Constants.credentials["users"]["real"]["pass"])
        Helpers.element_is_present(self, SideBarLoc.inbox_li_btn)

    def test_login_neg_bad_credentials(self):
        Login.login_form(self, Constants.credentials["users"]["fake"]["user"], Constants.credentials["users"]["fake"]["pass"])
        Helpers.element_contains_text(self, LoginLoc.inv_error_lbl, Constants.error_msg["bad_credentials"])

    def test_login_neg_bad_email(self):
        Login.login_form(self, None, Constants.credentials["users"]["fake"]["pass"])
        Helpers.element_contains_text(self, LoginLoc.email_error_lbl, Constants.error_msg["bad_email"])

    def test_login_neg_bad_password(self):
        Login.login_form(self, Constants.credentials["users"]["fake"]["user"], None)
        Helpers.element_contains_text(self, LoginLoc.pass_error_lbl, Constants.error_msg["bad_password"])

    def tearDown(self):
        Helpers.wait_seconds(self, 2)
        self.driver.quit()

    if __name__ == "__main__":
        unittest.main()
