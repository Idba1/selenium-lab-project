from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utilities.logger import get_logger


class CheckoutPage(BasePage):

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")

    CONTINUE_BUTTON = (By.ID, "continue")
    CANCEL_BUTTON = (By.ID, "cancel")

    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger(self.__class__.__name__)

    def fill_information(self, first, last, postal):

        self.logger.info("Entering checkout information")

        self.type(self.FIRST_NAME, first)
        self.type(self.LAST_NAME, last)
        self.type(self.POSTAL_CODE, postal)

    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)

    def continue_checkout(self, first, last, postal):

        self.fill_information(first, last, postal)

        self.click_continue()

    def get_error(self):
        return self.get_text(self.ERROR_MESSAGE)

    def click_cancel(self):
        self.click(self.CANCEL_BUTTON)
