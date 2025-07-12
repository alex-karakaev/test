import os
import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from ui.locators import basic_locators
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from _pytest.fixtures import FixtureRequest
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.cart_page import CartPage
from ui.pages.dashboard_page import DashboardPage
from ui.pages.login_page import LoginPage

CLICK_RETRY = 3

class BaseCase:

    driver = None
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, logger, request: FixtureRequest):
        self.driver: WebDriver = driver
        self.config = config
        self.logger = logger

        self.login_page = LoginPage(driver)
        if self.authorize:
            cookies = request.getfixturevalue('cookies')
            for cookie in cookies:
                self.driver.add_cookie(cookie)

            self.driver.refresh()
            self.main_page = MainPage(driver)
            self.login_page = LoginPage(driver)
            self.cart_page = CartPage(driver)
            self.dashboard_page = DashboardPage(driver)

        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.main_page: MainPage = request.getfixturevalue('main_page')
        self.cart_page: CartPage = request.getfixturevalue('cart_page')
        self.dashboard_page: DashboardPage = request.getfixturevalue('dashboard_page')

        self.logger.debug('Initial setup completed')
