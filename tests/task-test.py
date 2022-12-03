import unittest
from selenium import webdriver
from data.constants import Constants
from helpers.keywords import Helpers
from pom.pages.login import Login
from pom.pages.task import Task
from pom.locators.base_loc import BaseLoc
from pom.locators.home_loc import HomeLoc
from pom.locators.sidebar_loc import SideBarLoc


class TaskTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(Constants.url["prod"])
        self.driver.find_element(*BaseLoc.sign_in_lnk).click()
        Login.login_form(self, Constants.credentials["users"]["real"]["user"], Constants.credentials["users"]["real"]["pass"])
        Helpers.click_visible_element(self, SideBarLoc.inbox_li_btn)

    @unittest.skip
    def test_new_task_today(self):
        Task.add_new_task(self, Constants.tasks_data["name"], Constants.tasks_data["description"], Constants.dates["today"])
        Helpers.wait_seconds(self, 3)
        Helpers.element_is_present(self, HomeLoc.taskBodyElmnt)

    @unittest.skip
    def test_new_task_tomorrow(self):
        Task.add_new_task(self, Constants.tasks_data["name"], Constants.tasks_data["description"], Constants.dates["tomorrow"])
        Helpers.wait_seconds(self, 3)
        Helpers.element_is_present(self, HomeLoc.taskBodyElmnt)

    @unittest.skip
    def test_new_task_next_week(self):
        Task.add_new_task(self, Constants.tasks_data["name"], Constants.tasks_data["description"], Constants.dates["next"])
        Helpers.wait_seconds(self, 3)
        Helpers.element_is_present(self, HomeLoc.taskBodyElmnt)

    @unittest.skip
    def test_new_task_weekend(self):
        Task.add_new_task(self, Constants.tasks_data["name"], Constants.tasks_data["description"], Constants.dates["week"])
        Helpers.wait_seconds(self, 3)
        Helpers.element_is_present(self, HomeLoc.taskBodyElmnt)

    def test_delete_tasks(self):
        Task.delete_tasks(self)
        Helpers.wait_seconds(self, 3)

    # CREAR CLASE PARA MANEJAR HOOKS
    def tearDown(self):
        self.driver.quit()

    if __name__ == "__main__":
        unittest.main()

    # PARA CORRER PRUEBAS EN PARALELO
