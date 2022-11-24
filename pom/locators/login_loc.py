from selenium.webdriver.common.by import By


class LoginLoc(object):

    logInEmailInp = (By.ID, "element-0")
    logInPassInp = (By.ID, "element-3")
    logInBtn = (By.CSS_SELECTOR, "[data-gtm-id='start-email-login']")
    invErrorMsgLbl = (By.CSS_SELECTOR, "div.a83bd4e0._266d6623")
    emailErrorMsgLbl = (By.ID, "element-2")
    passErrorMsgLbl = (By.ID, "element-5")
