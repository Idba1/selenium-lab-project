import pytest
from utilities.screenshot import take_screenshot

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from config.config import Config
from utilities.logger import get_logger


logger = get_logger("Browser")


@pytest.fixture
def driver():
    logger.info("Launching Chrome Browser")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    driver.maximize_window()
    logger.info("Browser Maximized")

    driver.implicitly_wait(Config.IMPLICIT_WAIT)

    driver.get(Config.BASE_URL)
    logger.info(f"Navigated to {Config.BASE_URL}")

    yield driver

    logger.info("Closing Browser")
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            take_screenshot(driver, item.name)