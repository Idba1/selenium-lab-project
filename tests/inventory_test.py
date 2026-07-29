from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.config import Config


def test_add_single_product(driver):

    login = LoginPage(driver)

    login.login(
        Config.USERNAME,
        Config.PASSWORD
    )

    inventory = InventoryPage(driver)

    inventory.add_backpack()

    assert inventory.get_cart_badge() == "1"


def test_add_multiple_products(driver):

    login = LoginPage(driver)

    login.login(
        Config.USERNAME,
        Config.PASSWORD
    )

    inventory = InventoryPage(driver)

    inventory.add_backpack()

    inventory.add_bike_light()

    assert inventory.get_cart_badge() == "2"


def test_remove_product(driver):

    login = LoginPage(driver)

    login.login(
        Config.USERNAME,
        Config.PASSWORD
    )

    inventory = InventoryPage(driver)

    inventory.add_backpack()

    inventory.remove_backpack()

    assert inventory.driver.find_elements(*inventory.CART_BADGE) == []


def test_open_cart(driver):

    login = LoginPage(driver)

    login.login(
        Config.USERNAME,
        Config.PASSWORD
    )

    inventory = InventoryPage(driver)

    inventory.open_cart()

    assert "cart.html" in driver.current_url
