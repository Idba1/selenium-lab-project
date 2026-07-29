from wrappers.selenium_wrapper import SeleniumWrapper


class BasePage(SeleniumWrapper):

    def __init__(self, driver):
        super().__init__(driver)
