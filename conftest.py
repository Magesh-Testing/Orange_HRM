import logging

import os
from datetime import datetime
import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        driver = item.funcargs.get("setup_driver")

        if driver:
            status = "PASS" if report.passed else "FAIL"

            screenshots_dir = f"screenshots/{status}"
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            test_name = report.nodeid.replace("::", "_").replace("/", "_")
            screenshot_path = f"{screenshots_dir}/{test_name}_{timestamp}.png"

            driver.save_screenshot(screenshot_path)
            print(f"\nScreenshot ({status}) saved: {screenshot_path}")

def pytest_configure():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    file_handler = logging.FileHandler("test_logs.log")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

def pytest_addoption(parser):
    parser.addoption("--browser-name", default = "firefox", help = "Choose browser name ")

@pytest.fixture(scope="class")
def setup_driver(request):
    #Default browser is Firefox
    browser_name = request.config.getoption("--browser-name")
    if browser_name.lower() == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    elif browser_name.lower() == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    elif browser_name.lower() == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

    elif browser_name.lower() == "safari":
        driver = webdriver.safari()

    else:
        raise ValueError(f"Browser {browser_name} not supported")
    driver.maximize_window()
    yield driver
    try:
        driver.quit()
    except Exception:
        print("Error quitting the driver")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        if "setup_driver" in item.fixturenames:
            driver = item.funcargs["setup_driver"]
            driver.save_screenshot(f"screenshot_{item.name}.png")