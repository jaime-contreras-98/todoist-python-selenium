from pom.locators.login_loc import LoginLoc


class Login(object):

    def __init__(self, driver):
        self.driver = driver

    def login_form(self, user, password):
        if user is not None:
            self.driver.find_element(*LoginLoc.logInEmailInp).send_keys(user)
        if password is not None:
            self.driver.find_element(*LoginLoc.logInPassInp).send_keys(password)
        self.driver.find_element(*LoginLoc.logInBtn).click()

