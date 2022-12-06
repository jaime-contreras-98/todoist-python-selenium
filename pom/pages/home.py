from selenium.common.exceptions import NoSuchElementException
from pom.locators.home_loc import HomeLoc
from helpers.keywords import Helpers
from data.constants import Constants


class Home(object):

    def __init__(self, driver):
        self.driver = driver

    def create_sections(self, no_sections, name):
        for x in range(no_sections):
            self.driver.find_element(*HomeLoc.new_section_btn).click()
            self.driver.find_element(*HomeLoc.section_name_inp).send_keys(name + ' - ' + (str(+x)))
            self.driver.find_element(*HomeLoc.add_section_btn).click()

    def delete_all_sections(self):
        try:
            while self.driver.find_element(*HomeLoc.section_body_elmnt):
                self.driver.find_element(*HomeLoc.section_menu_btn).click()
                self.driver.find_element(*HomeLoc.section_menu_delete_btn).click()
                self.driver.find_element(*HomeLoc.section_delete_confirm_btn).click()
        except NoSuchElementException:
            print("No more sections found")

    def validate_project(self):
        Helpers.wait_seconds(self, 1)
        project_name = self.driver.find_element(*HomeLoc.header_lbl).text

        if project_name.__contains__(Constants.project_data["name"]):
            print("Both elements match!")
            assert True
        else:
            print("Elements does not match!")
            assert False
