from selenium.webdriver.common.by import By


class HomeLoc(object):
    headerLabel = (By.CLASS_NAME, "simple_content")
    newTaskBtn = (By.CLASS_NAME, "plus_add_button")
    dateTaskBtn = (By.CLASS_NAME, "item_due_selector")
    projTypeTaskBtn = (By.CSS_SELECTOR, "button[aria-owns='dropdown-select-37-popup']")
    todayTaskBtn = (By.CSS_SELECTOR, "button[data-track*='today']")
    tomorrowTaskBtn = (By.CSS_SELECTOR, "button[data-track*='tomorrow']")
    weekendTaskBtn = (By.CSS_SELECTOR, "button[data-track*='weekend']")
    nextWeekTaskBtn = (By.CSS_SELECTOR, "button[data-track*='nextweek']")
    addTaskBtn = (By.CSS_SELECTOR, "button[data-testid='task-editor-submit-button']")
    taskNameInp = (By.CLASS_NAME, "public-DraftStyleDefault-block")
    taskDescInp = (By.CLASS_NAME, "task_editor__description_field")
    taskBodyElmnt = (By.CLASS_NAME, "task_list_item__body")


