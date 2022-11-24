from selenium.webdriver.common.by import By


class BaseLoc(object):

    signInLink = (By.CSS_SELECTOR, ".mFaV87MJWaQZl7X1C1h7 > li:nth-child(1)")
    signUpLink = (By.CSS_SELECTOR, ".mFaV87MJWaQZl7X1C1h7 > li:nth-child(2)")
