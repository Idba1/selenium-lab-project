from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utilities.logger import get_logger
from selenium.webdriver.support import expected_conditions as EC

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

        logout_btn = self.wait.until(
            EC.visibility_of_element_located(self.LOGOUT_BUTTON)
        )

        # Debug
        print("Logout displayed:", logout_btn.is_displayed())
        print("Logout enabled:", logout_btn.is_enabled())

        # JavaScript click
        self.driver.execute_script("arguments[0].click();", logout_btn)

    def logout(self):
        self.logger.info("Logout started")

        self.click_menu()

        self.wait.until(
            EC.element_to_be_clickable(self.LOGOUT_BUTTON)
        )

        self.click_logout()

        self.wait.until(
            EC.url_contains("saucedemo.com")
        )

        self.logger.info("Logout completed")
