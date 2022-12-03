from selenium.common.exceptions import NoSuchElementException
from pom.locators.home_loc import HomeLoc
from helpers.keywords import Helpers


class Task(object):

    def __init__(self, driver):
        self.driver = driver

    def add_new_task(self, task_name, task_desc, date):
        self.driver.find_element(*HomeLoc.new_task_btn).click()
        self.driver.find_element(*HomeLoc.task_name_inp).send_keys(task_name)
        self.driver.find_element(*HomeLoc.task_desc_inp).send_keys(task_desc)
        self.driver.find_element(*HomeLoc.choose_date_btn).click()
        Helpers.find_dynamic_element_click(self, HomeLoc.task_date_btn, date)
        self.driver.find_element(*HomeLoc.add_task_btn).click()

    def delete_tasks(self):
        try:
            while self.driver.find_element(*HomeLoc.task_body_elmnt):
                self.driver.find_element(*HomeLoc.task_body_elmnt).click()
                self.driver.find_element(*HomeLoc.task_actions_btn).click()
                self.driver.find_element(*HomeLoc.task_menu_delete_btn).click()
                self.driver.find_element(*HomeLoc.task_delete_btn).click()
        except NoSuchElementException:
            print("No tasks found")

