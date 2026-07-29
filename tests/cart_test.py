from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from config.config import Config


def test_product_visible_in_cart(driver):

    login = LoginPage(driver)

    login.login(
        Config.USERNAME,
        Config.PASSWORD
    )

    inventory = InventoryPage(driver)

    inventory.add_backpack()

    inventory.open_cart()

    cart = CartPage(driver)

    assert cart.backpack_exists()


def test_continue_shopping(driver):

    login = LoginPage(driver)

    login.login(
        Config.USERNAME,
        Config.PASSWORD
    )

    inventory = InventoryPage(driver)

    inventory.add_backpack()

    inventory.open_cart()

    cart = CartPage(driver)

    cart.continue_shopping()

    assert "inventory.html" in driver.current_url


def test_remove_from_cart(driver):

    login = LoginPage(driver)

    login.login(
        Config.USERNAME,
        Config.PASSWORD
    )

    inventory = InventoryPage(driver)

    inventory.add_backpack()

    inventory.open_cart()

    cart = CartPage(driver)

    cart.remove_backpack()

    assert not cart.backpack_exists()
