import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from pom.locators.sidebar_loc import SideBarLoc
from helpers.keywords import Helpers


class Project(object):

    def __init__(self, driver):
        self.driver = driver

    def create_projects(self, no_tasks, name, favorite, view_word):
        random_number = random.randint(0, 21)
        action = ActionChains(self.driver)
        number_tasks = no_tasks

        for x in range(number_tasks):
            self.driver.find_element(*SideBarLoc.new_project_btn).click()
            self.driver.find_element(*SideBarLoc.project_name_inp).send_keys(name + " - " + (str(+x)))
            self.driver.find_element(*SideBarLoc.project_color_btn).click()
            for j in range(random_number + x):
                action.send_keys(Keys.DOWN).perform()
            action.send_keys(Keys.ENTER).perform()
            if favorite:
                self.driver.find_element(*SideBarLoc.project_fav_switch).click()
            Helpers.find_dynamic_element_click(self, SideBarLoc.project_view_btn, view_word)
            self.driver.find_element(*SideBarLoc.project_new_add_btn).click()

    def delete_all_projects(self):
        try:
            while self.driver.find_element(*SideBarLoc.project_body_elmnt):
                self.driver.find_element(*SideBarLoc.project_body_elmnt).click()
                self.driver.find_element(*SideBarLoc.project_actions_btn).click()
                self.driver.find_element(*SideBarLoc.project_actions_delete_btn).click()
                self.driver.find_element(*SideBarLoc.project_actions_confirm_btn).click()
        except NoSuchElementException:
            print("No projects found")

    def validate_task(self, name):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, name)
