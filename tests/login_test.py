from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.config import Config
from utilities.logger import get_logger


logger = get_logger("Test")


def test_valid_login(driver):

    logger.info("========== test_valid_login Started ==========")

    login_page = LoginPage(driver)

    login_page.login(
        Config.USERNAME,
        Config.PASSWORD
    )

    inventory_page = InventoryPage(driver)

    assert inventory_page.get_page_title() == "Products"
    # assert inventory_page.get_page_title() == "Home"

    logger.info("========== test_valid_login Passed ==========")


def test_logout(driver):

    logger.info("========== test_logout Started ==========")

    login_page = LoginPage(driver)

    login_page.login(
        Config.USERNAME,
        Config.PASSWORD
    )

    inventory_page = InventoryPage(driver)

    inventory_page.logout()

    assert driver.current_url == Config.BASE_URL

    logger.info("========== test_logout Passed ==========")