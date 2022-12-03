from selenium.webdriver.common.by import By


class LoginLoc(object):

    login_email_inp = (By.ID, "element-0")
    login_pass_inp = (By.ID, "element-3")
    login_btn = (By.CSS_SELECTOR, "[data-gtm-id='start-email-login']")
    inv_error_lbl = (By.CSS_SELECTOR, "div.a83bd4e0._266d6623")
    email_error_lbl = (By.ID, "element-2")
    pass_error_lbl = (By.ID, "element-5")
