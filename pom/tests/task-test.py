import unittest
from selenium import webdriver
from data.constants import Constants
from helpers.keywords import Helpers
from pom.pages.login import Login
from pom.pages.home import Home
from pom.locators.base_loc import BaseLoc
from pom.locators.home_loc import HomeLoc
from pom.locators.sidebar_loc import SideBarLoc


class TaskTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(Constants.url[0])
        self.driver.find_element(*BaseLoc.signInLink).click()
        Login.login_form(self, Constants.credentials["users"]["real"]["user"], Constants.credentials["users"]["real"]["pass"])
        Helpers.click_visible_element(self, SideBarLoc.inboxLiBtn)

    def test_new_task_today(self):
        Home.add_new_task(self, Constants.tasks_data[0], Constants.tasks_data[1], Constants.dates[0])
        Helpers.element_is_present(self, HomeLoc.taskBodyElmnt)

    def test_new_task_tomorrow(self):
        Home.add_new_task(self, Constants.tasks_data[0], Constants.tasks_data[1], Constants.dates[1])

    def tearDown(self):
        self.driver.quit()

    if __name__ == "__main__":
        unittest.main()
