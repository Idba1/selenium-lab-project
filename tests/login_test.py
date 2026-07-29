from pages.login_page import LoginPage
from config.config import Config


def test_valid_login(driver):

    login_page = LoginPage(driver)

    login_page.login(
        Config.USERNAME,
        Config.PASSWORD
    )

    assert "inventory" in driver.current_url
