from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utilities.logger import get_logger


class CheckoutCompletePage(BasePage):

    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    # BACK_HOME = (By.ID, "back-to-products")
    BACK_HOME = (By.ID, "back-to-products")

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger(self.__class__.__name__)

    def success_message(self):
        return self.get_text(self.COMPLETE_HEADER)

    # def back_home(self):
    #     self.click(self.BACK_HOME)

    def back_home(self):
        self.logger.info("Clicking Back Home")
        self.click(self.BACK_HOME)
