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
from ui.pages.search_page import SearchPage

CLICK_RETRY = 3

class BaseCase:

    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def ui_report(self, driver, request, temp_dir):
        failed_tests_count = request.session.testsfailed
        yield
        if request.session.testsfailed > failed_tests_count:
            driver.get_screenshot_as_file(os.path.join(temp_dir, 'failure.png'))

            with open(os.path.join(temp_dir, 'browser.log'), 'w') as f:
                for i in driver.get_log('browser'):
                    f.write(f"{i['level']} - {i['source']}\n{i['message']}\n")

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, logger, request: FixtureRequest):
        self.driver: WebDriver = driver
        self.config = config
        self.logger = logger

        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.main_page: MainPage = request.getfixturevalue('main_page')
        self.search_page: SearchPage = request.getfixturevalue('search_page')

        self.logger.debug('Initial setup completed')
