from pom.locators.login_loc import LoginLoc


class Login(object):

    context = None

    def __init__(self, context, driver):
        self.context = context
        self.driver = driver

    def login_form(self, user, password):
        if user is not None:
            self.driver.find_element(*LoginLoc.login_email_inp).send_keys(user)
        if password is not None:
            self.driver.find_element(*LoginLoc.login_pass_inp).send_keys(password)
        self.driver.find_element(*LoginLoc.login_btn).click()

