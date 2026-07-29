from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from config.config import Config


def test_empty_first_name(driver):

    LoginPage(driver).login(
        Config.USERNAME,
        Config.PASSWORD
    )

    inventory = InventoryPage(driver)
    inventory.add_backpack()
    inventory.open_cart()

    cart = CartPage(driver)
    cart.click_checkout()

    checkout = CheckoutPage(driver)

    checkout.continue_checkout(
        "",
        "Islam",
        "1340"
    )

    assert checkout.get_error() == "Error: First Name is required"


def test_empty_last_name(driver):

    LoginPage(driver).login(
        Config.USERNAME,
        Config.PASSWORD
    )

    inventory = InventoryPage(driver)
    inventory.add_backpack()
    inventory.open_cart()

    CartPage(driver).click_checkout()

    checkout = CheckoutPage(driver)

    checkout.continue_checkout(
        "Monira",
        "",
        "1340"
    )

    assert checkout.get_error() == "Error: Last Name is required"


def test_empty_postal_code(driver):

    LoginPage(driver).login(
        Config.USERNAME,
        Config.PASSWORD
    )

    inventory = InventoryPage(driver)
    inventory.add_backpack()
    inventory.open_cart()

    CartPage(driver).click_checkout()

    checkout = CheckoutPage(driver)

    checkout.continue_checkout(
        "Monira",
        "Islam",
        ""
    )

    assert checkout.get_error() == "Error: Postal Code is required"


def test_cancel_checkout(driver):

    LoginPage(driver).login(
        Config.USERNAME,
        Config.PASSWORD
    )

    inventory = InventoryPage(driver)
    inventory.add_backpack()
    inventory.open_cart()

    CartPage(driver).click_checkout()

    checkout = CheckoutPage(driver)

    checkout.click_cancel()

    assert "cart.html" in driver.current_url


def test_back_home(driver):

    LoginPage(driver).login(
        Config.USERNAME,
        Config.PASSWORD
    )

    inventory = InventoryPage(driver)

    inventory.add_backpack()
    inventory.open_cart()

    CartPage(driver).click_checkout()

    checkout = CheckoutPage(driver)

    checkout.continue_checkout(
        "Monira",
        "Islam",
        "1340"
    )

    from pages.checkout_overview_page import CheckoutOverviewPage

    overview = CheckoutOverviewPage(driver)

    overview.click_finish()

    from pages.checkout_complete_page import CheckoutCompletePage

    complete = CheckoutCompletePage(driver)

    complete.back_home()

    assert "inventory.html" in driver.current_url
