from selenium.webdriver.common.by import By
from wrappers.selenium_wrapper import SeleniumWrapper


class InventoryPage(SeleniumWrapper):

    PAGE_TITLE = (By.CLASS_NAME, "title")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_BUTTON = (By.ID, "logout_sidebar_link")

    def __init__(self, driver):
        super().__init__(driver)

    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)

    def click_menu(self):
        self.click(self.MENU_BUTTON)

    def click_logout(self):
        self.click(self.LOGOUT_BUTTON)

    def logout(self):
        self.click_menu()
        self.click_logout()
