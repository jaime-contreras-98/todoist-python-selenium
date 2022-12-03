from selenium.webdriver.common.by import By


class BaseLoc(object):

    sign_in_lnk = (By.CSS_SELECTOR, ".mFaV87MJWaQZl7X1C1h7 > li:nth-child(1)")
    sign_up_lnk = (By.CSS_SELECTOR, ".mFaV87MJWaQZl7X1C1h7 > li:nth-child(2)")
