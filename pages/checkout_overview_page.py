from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utilities.logger import get_logger
from selenium.webdriver.support import expected_conditions as EC


class CheckoutOverviewPage(BasePage):

    FINISH_BUTTON = (By.ID, "finish")

    TITLE = (By.CLASS_NAME, "title")

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger(self.__class__.__name__)

    # def click_finish(self):
    #     self.click(self.FINISH_BUTTON)

    def click_finish(self):

        self.wait.until(
            EC.element_to_be_clickable(self.FINISH_BUTTON)
        )

        self.click(self.FINISH_BUTTON)

    def get_title(self):
        return self.get_text(self.TITLE)
