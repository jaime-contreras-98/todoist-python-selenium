from selenium.common.exceptions import NoSuchElementException
from pom.locators.home_loc import HomeLoc
from helpers.keywords import Helpers
from data.constants import Constants


class Task(object):

    def __init__(self, driver):
        self.driver = driver

    def create_tasks(self, no_tasks, task_name, task_desc, date):
        self.driver.find_element(*HomeLoc.new_task_btn).click()
        for x in range(no_tasks):
            self.driver.find_element(*HomeLoc.task_name_inp).send_keys(task_name + ' - ' + (str(+x)))
            self.driver.find_element(*HomeLoc.task_desc_inp).send_keys(task_desc)
            self.driver.find_element(*HomeLoc.choose_date_btn).click()
            Helpers.find_dynamic_element_click(self, HomeLoc.task_date_btn, date)
            self.driver.find_element(*HomeLoc.add_task_btn).click()

    def delete_all_tasks(self):
        try:
            while self.driver.find_element(*HomeLoc.task_body_elmnt):
                self.driver.find_element(*HomeLoc.task_body_elmnt).click()
                self.driver.find_element(*HomeLoc.task_actions_btn).click()
                self.driver.find_element(*HomeLoc.task_menu_delete_btn).click()
                self.driver.find_element(*HomeLoc.task_delete_btn).click()
        except NoSuchElementException:
            print("No tasks found")

    def validate_task(self):
        Helpers.wait_seconds(self, 1)
        self.driver.find_element(*HomeLoc.task_last_body_elmnt).click()
        task_name = self.driver.find_element(*HomeLoc.header_task_lbl).text

        if task_name.__contains__(Constants.tasks_data["name"]):
            print("Both elements match!")
            self.driver.find_element(*HomeLoc.task_close_menu_btn).click()
            assert True
        else:
            print("Elements does not match!")
            assert False

