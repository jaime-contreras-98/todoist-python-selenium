from pom.locators.home_loc import HomeLoc


class Home(object):

    def __init__(self, driver):
        self.driver = driver

    def add_new_task(self, task_name, task_desc, date):
        self.driver.find_element(*HomeLoc.newTaskBtn).click()
        self.driver.find_element(*HomeLoc.taskNameInp).send_keys(task_name)
        self.driver.find_element(*HomeLoc.taskDescInp).send_keys(task_desc)
        self.driver.find_element(*HomeLoc.dateTaskBtn).click()
        match date:
            case 'Today':
                self.driver.find_element(*HomeLoc.todayTaskBtn).click()
            case 'Tomorrow':
                self.driver.find_element(*HomeLoc.tomorrowTaskBtn).click()
            case 'Weekend':
                self.driver.find_element(*HomeLoc.weekendTaskBtn).click()
            case 'Next Week':
                self.driver.find_element(*HomeLoc.nextWeekTaskBtn).click()
            case _:
                print('Invalid Option!!')
        self.driver.find_element(*HomeLoc.addTaskBtn).click()

    def add_multiple_tasks(self, task_name, task_desc, date, number):
        print("")
