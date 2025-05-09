import os
import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import attachment
from dotenv import load_dotenv


@pytest.fixture(scope="session", autouse=True)
def setup_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = 'https://yasno.live'
    browser.config.timeout = 10000

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "127.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    SELENOID_LOGIN = os.getenv("SELENOID_LOGIN")
    SELENOID_PASSWORD = os.getenv("SELENOID_PASSWORD")
    SELENOID_URL = os.getenv("SELENOID_URL")

    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--incognito")

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://{SELENOID_LOGIN}:{SELENOID_PASSWORD}@{SELENOID_URL}/wd/hub",
        options=options
    )
    browser.config.driver = driver

    yield

    attachment.add_screenshot(browser)
    attachment.add_logs(browser)
    attachment.add_html(browser)
    attachment.add_video(browser)

    browser.quit()