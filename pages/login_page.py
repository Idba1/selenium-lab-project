from utilities.logger import get_logger
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger(self.__class__.__name__)

    def enter_username(self, username):
        self.logger.info("Entering username")
        self.type(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.logger.info("Entering password")
        self.type(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.logger.info("Clicking Login button")
        self.click(self.LOGIN_BUTTON)

    def login(self, username, password):
        self.logger.info("Login process started")

        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

        self.logger.info("Login process completed")
