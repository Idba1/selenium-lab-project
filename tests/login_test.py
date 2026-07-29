from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.config import Config


def test_valid_login(driver):

    login_page = LoginPage(driver)

    login_page.login(
        Config.USERNAME,
        Config.PASSWORD
    )

    inventory_page = InventoryPage(driver)

    assert inventory_page.get_page_title() == "Products"


def test_logout(driver):

    login_page = LoginPage(driver)

    login_page.login(
        Config.USERNAME,
        Config.PASSWORD
    )

    inventory_page = InventoryPage(driver)

    inventory_page.logout()

    assert driver.current_url == Config.BASE_URL
