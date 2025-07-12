import time
import pytest
from _pytest.fixtures import FixtureRequest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ui.fixtures import *
from ui.locators import basic_locators
from base import BaseCase
from ui.pages.base_page import BasePage
from ui.pages.login_page import *
from ui import urls

# class BaseCase():
#     authorize = True
#
#     @pytest.fixture(scope='function', autouse=True)
#     def setup(self, driver, config, request: FixtureRequest, logger):
#         self.driver = driver
#         self.config = config
#         self.logger = logger
#
#         self.login_page = LoginPage(driver)
#         if self.authorize:
#             cookies = request.getfixturevalue('cookies')
#             for cookie in cookies:
#                 self.driver.add_cookie(cookie)
#
#             self.driver.refresh()
#             self.main_page = MainPage(driver)

class TestLogin(BaseCase):
    authorize = False

    @pytest.mark.skip("SKIP")
    def test_login(self, credentials, authorize=False):
        login_page = LoginPage(self.driver)
        login_page.login(*credentials)

class TestLK(BaseCase):

    @pytest.mark.skip("SKIP")
    def test_lk(self):
        time.sleep(2)

    @pytest.mark.skip("SKIP")
    def test_check_cart(self):
        self.cart_page.cart_check()
        assert 'Sleeveless Dress' in self.driver.page_source
        self.base_page.check_url(urls.URL_CART)

    @pytest.mark.skip("SKIP")
    def test_delete(self):
        self.cart_page.cart_delete()
        assert 'Cart is empty!' in self.driver.page_source




