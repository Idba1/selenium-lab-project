from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utilities.logger import get_logger


class CartPage(BasePage):

    CART_TITLE = (By.CLASS_NAME, "title")

    BACKPACK = (By.ID, "item_4_title_link")

    CONTINUE_SHOPPING = (By.ID, "continue-shopping")

    CHECKOUT = (By.ID, "checkout")

    REMOVE_BACKPACK = (By.ID, "remove-sauce-labs-backpack")

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger(self.__class__.__name__)

    def get_title(self):
        return self.get_text(self.CART_TITLE)

    def click_checkout(self):
        self.click(self.CHECKOUT)

    def continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING)

    def remove_backpack(self):
        self.click(self.REMOVE_BACKPACK)

    def backpack_exists(self):
        return self.is_element_present(self.BACKPACK)
