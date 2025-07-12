import time
import pytest
from _pytest.fixtures import FixtureRequest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ui.fixtures import *
from ui.locators import basic_locators

class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest, logger):
        self.driver = driver
        self.config = config
        self.logger = logger

        self.login_page = LoginPage(driver)
        if self.authorize:
            cookies = request.getfixturevalue('cookies')
            for cookie in cookies:
                self.driver.add_cookie(cookie)

            self.driver.refresh()
            self.main_page = MainPage(driver)


@pytest.fixture(scope='session')
def credentials():
    with open('user1.txt') as f:
        user = f.readline().strip()
        password = f.readline().strip()

    return user, password


class LoginPage(BasePage):
    url = 'https://automationexercise.com/'

    def login(self, user, password):
        cookies_button = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(basic_locators.BasePageLocators.COOKIES_SUBMIT_BUTTON_LOCATOR)
        )
        cookies_button.click()

        self.click(basic_locators.BasePageLocators.LOGIN_LOCATOR)
        self.find(basic_locators.LoginPageLocators.LOGIN_LINE_LOCATOR).send_keys(user)
        self.find(basic_locators.LoginPageLocators.PASSWORD_LINE_LOCATOR).send_keys(password)

        self.click(basic_locators.LoginPageLocators.SUBMIT_BUTTON_LOCATOR)

        time.sleep(5)
        return MainPage(self.driver)


class MainPage(BasePage):
    url = 'https://automationexercise.com/'


class TestLogin(BaseCase):
    authorize = False

    @pytest.mark.skip("SKIP")
    def test_login(self, credentials):
        login_page = LoginPage(self.driver)
        login_page.login(*credentials)

        time.sleep(5)

class TestLK(BaseCase):

    @pytest.mark.skip("SKIP")
    def test_lk(self):
        time.sleep(3)

    def test_cart(self):
        self.driver.click(basic_locators.MainPageLocators.DRESS_ADD_BUTTON)
        self.driver.click(basic_locators.CartPageLocators.VIEW_CART_BUTTON)

