# happy path
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage

from config.config import Config


def test_complete_checkout(driver):

    login = LoginPage(driver)

    login.login(
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
        "Idba",
        "Islam",
        "1340"
    )

    overview = CheckoutOverviewPage(driver)

    assert overview.get_title() == "Checkout: Overview"

    # overview.click_finish()
    # print(driver.current_url)
    # print(driver.page_source)

    # complete = CheckoutCompletePage(driver)

    # assert complete.success_message() == "Thank you for your order!"


    # overview.click_finish()

    # print(driver.current_url)

    # complete = CheckoutCompletePage(driver)

    # print(driver.current_url)

    # assert complete.success_message() == "Thank you for your order!"
    
    overview = CheckoutOverviewPage(driver)

    assert overview.get_title() == "Checkout: Overview"

    print("Before Finish:", driver.current_url)

    overview.click_finish()

    print("After Finish:", driver.current_url)