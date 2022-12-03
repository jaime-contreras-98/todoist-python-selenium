import unittest
from selenium import webdriver
from data.constants import Constants
from helpers.keywords import Helpers
from pom.pages.login import Login
from pom.pages.project import Project
from pom.locators.base_loc import BaseLoc
from pom.locators.home_loc import HomeLoc
from pom.locators.sidebar_loc import SideBarLoc


class ProjectTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(Constants.url["prod"])
        self.driver.find_element(*BaseLoc.sign_in_lnk).click()
        Login.login_form(self, Constants.credentials["users"]["real"]["user"], Constants.credentials["users"]["real"]["pass"])
        Helpers.click_visible_element(self, SideBarLoc.inbox_li_btn)

    def test_create_project(self):
        Project.create_projects(self, 1, Constants.project_data["name"], False, Constants.project_data["view"]["panel"])
        Helpers.element_contains_partial_text(self, HomeLoc.header_lbl, Constants.project_data["name"])

    def test_create_project_fav(self):
        Project.create_projects(self, 2, Constants.project_data["name"], True, Constants.project_data["view"]["list"])

    def test_delete_all_projects(self):
        Project.delete_all_projects(self)

    def tearDown(self):
        Helpers.wait_seconds(self, 3)
        self.driver.quit()

    if __name__ == "__main__":
        unittest.main()
