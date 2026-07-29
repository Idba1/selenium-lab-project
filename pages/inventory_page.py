from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utilities.logger import get_logger

class InventoryPage(BasePage):

    PAGE_TITLE = (By.CLASS_NAME, "title")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_BUTTON = (By.ID, "logout_sidebar_link")

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger(self.__class__.__name__)

    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)

    def click_menu(self):
        self.logger.info("Opening side menu")
        self.click(self.MENU_BUTTON)

    def click_logout(self):
        self.logger.info("Clicking Logout")
        self.click(self.LOGOUT_BUTTON)

    def logout(self):
        self.logger.info("Logout started")

        self.click_menu()
        self.click_logout()

        self.logger.info("Logout completed")
