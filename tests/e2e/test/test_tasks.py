import unittest
from selenium import webdriver
from data.constants import Constants
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from helpers.keywords import Helpers
from pom.pages.task import Task
from pom.pages.login import Login
from pom.locators.base_loc import BaseLoc
from pom.locators.sidebar_loc import SideBarLoc


class TaskTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.headless = True
        print("========== TASKS TESTS ==========")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.maximize_window()
        self.driver.get(Constants.url["prod"])
        self.driver.find_element(*BaseLoc.sign_in_lnk).click()
        Login.login_form(self, Constants.credentials["users"]["real"]["user"], Constants.credentials["users"]["real"]["pass"])
        Helpers.click_visible_element(self, SideBarLoc.inbox_li_btn)

    def test_new_task_today(self):
        Task.create_tasks(self, 1, Constants.tasks_data["name"], Constants.tasks_data["description"], Constants.dates["today"])
        Task.validate_task(self)

    def test_new_task_tomorrow(self):
        Task.create_tasks(self, 1, Constants.tasks_data["name"], Constants.tasks_data["description"], Constants.dates["tomorrow"])
        Task.validate_task(self)

    def test_new_task_next_week(self):
        Task.create_tasks(self, 1, Constants.tasks_data["name"], Constants.tasks_data["description"], Constants.dates["next"])
        Task.validate_task(self)

    def test_new_task_weekend(self):
        Task.create_tasks(self, 1, Constants.tasks_data["name"], Constants.tasks_data["description"], Constants.dates["week"])
        Task.validate_task(self)

    def test_new_tasks(self):
        Task.create_tasks(self, 3, Constants.tasks_data["name"], Constants.tasks_data["description"], Constants.dates["week"])
        Task.validate_task(self)

    def test_delete_tasks(self):
        Task.delete_all_tasks(self)

    # CREAR CLASE PARA MANEJAR HOOKS
    def tearDown(self):
        Helpers.wait_seconds(self, 3)
        self.driver.quit()

    if __name__ == "__main__":
        unittest.main()

    # PARA CORRER PRUEBAS EN PARALELO
