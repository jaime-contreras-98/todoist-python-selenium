from pom.locators.home_loc import HomeLoc


class Home(object):

    def __init__(self, driver):
        self.driver = driver

    def create_section(self, name):
        self.driver.find_element(*HomeLoc.new_section_btn).click()
        self.driver.find_element(*HomeLoc.section_name_inp).send_keys(name)
        self.driver.find_element(*HomeLoc.add_section_btn).click()
