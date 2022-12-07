from selenium.webdriver.common.by import By


class HomeLoc(object):
    header_lbl = (By.CSS_SELECTOR, "h1 > span.simple_content")
    header_task_lbl = (By.CSS_SELECTOR, ".task-overview-content > div.task_content")
    new_task_btn = (By.CLASS_NAME, "plus_add_button")
    new_section_btn = (By.CLASS_NAME, "hover_action_button")
    choose_date_btn = (By.CLASS_NAME, "item_due_selector")
    proj_task_btn = (By.CSS_SELECTOR, "button[aria-owns='dropdown-select-37-popup']")
    add_task_btn = (By.CSS_SELECTOR, "button[data-testid='task-editor-submit-button']")
    add_section_btn = (By.CSS_SELECTOR, "div.actions > button:nth-child(1)")
    task_menu_btn = (By.CLASS_NAME, "more_actions_button")
    task_close_menu_btn = (By.CSS_SELECTOR, "div[class='c6a2474f f53218d5'] > :not(button[id*=id-])")
    task_menu_delete_btn = (By.CSS_SELECTOR, "div[role='menu'] button:nth-child(8)")
    task_delete_btn = (By.CSS_SELECTOR, "footer[class] > div > button:nth-child(2)")
    task_actions_btn = (By.CSS_SELECTOR, "div.c6a2474f.f53218d5 > button[id*=id]")
    task_name_inp = (By.CSS_SELECTOR, "div[class*='no-focus-marker'] > div > div > div > p")
    task_desc_inp = (By.CSS_SELECTOR, "div[class*='task_editor__description_field'] > div > p")
    section_name_inp = (By.CSS_SELECTOR, "input.name")
    section_body_elmnt = (By.XPATH, "//li[@data-section-id!='_']")
    section_menu_btn = (By.CLASS_NAME, "section_head_menu")
    section_menu_delete_btn = (By.CSS_SELECTOR, ".menu_list > li:nth-last-child(1)")
    section_delete_confirm_btn = (By.CSS_SELECTOR, "button[data-autofocus='true']")
    task_body_elmnt = (By.XPATH, "//ul[@class='items'] //li[@id!='task-']")
    task_last_body_elmnt = (By.CSS_SELECTOR, ".items > li:nth-last-child(2)")

    # DYNAMIC SELECTORS
    task_date_btn = "button[data-track*=" + "TEXT" + "]"


