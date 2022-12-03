from selenium.webdriver.common.by import By


class SideBarLoc(object):
    inbox_li_btn = (By.ID, "filter_inbox")
    new_project_btn = (By.CSS_SELECTOR, "div.I0d9ZtQ > div:nth-child(2) > button")
    project_name_inp = (By.ID, "edit_project_modal_field_name")
    project_color_btn = (By.CLASS_NAME, "color_dropdown_toggle")
    project_color_elmnt = (By.XPATH, "//ul[@role='listbox'] //li")
    project_body_elmnt = (By.XPATH, "//ul[@id='projects_list'] //li")
    project_fav_switch = (By.CLASS_NAME, "reactist_switch")
    project_view_list_btn = (By.ID, "project_list_view_style_option")
    project_view_panel_btn = (By.ID, "project_list_board_style_option")
    project_new_add_btn = (By.CSS_SELECTOR, "button[type='submit']")
    project_actions_btn = (By.CSS_SELECTOR, "div.view_header__actions > button:nth-child(4)")
    project_actions_delete_btn = (By.CSS_SELECTOR, "div.popper > ul > li:nth-child(15)")
    project_actions_confirm_btn = (By.CSS_SELECTOR, "div.e90b43fb > button:nth-child(2)")

    # DYNAMIC LOCATORS, USE 'TEXT' TO MAKE THIS WORK
    project_view_btn = "label[id*=project_" + "TEXT" + "]"
