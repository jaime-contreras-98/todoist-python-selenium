import unittest
from selenium import webdriver
from data.constants import Constants
from helpers.keywords import Helpers
from pom.pages.login import Login
from pom.pages.home import Home
from pom.locators.base_loc import BaseLoc
from pom.locators.sidebar_loc import SideBarLoc


class SectionTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(Constants.url["prod"])
        self.driver.find_element(*BaseLoc.sign_in_lnk).click()
        Login.login_form(self, Constants.credentials["users"]["real"]["user"], Constants.credentials["users"]["real"]["pass"])
        Helpers.click_visible_element(self, SideBarLoc.inbox_li_btn)

    def test_create_section(self):
        Home.create_section(self, Constants.section_data["name"])

    def tearDown(self):
        Helpers.wait_seconds(self, 5)
        self.driver.quit()

    if __name__ == "__main__":
        unittest.main()
