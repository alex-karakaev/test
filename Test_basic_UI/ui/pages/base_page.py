import logging
import time

import pytest
from selenium.webdriver import ActionChains

from ui.locators import basic_locators
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

CLICK_RETRY = 3
BASE_TIMEOUT = 10


class PageNotLoadException(Exception):
    pass


class BasePage(object):
    #url = 'https://www.python.org/'
    locators = basic_locators.BasePageLocators

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger('test')
        self.is_opened()

    def is_opened(self, timeout=BASE_TIMEOUT):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == self.url:
                return True

        raise PageNotLoadException(f'{self.url} did not open in {timeout} sec for {self.__class__.__name__}.\n'
                                   f'Current url: {self.driver.current_url}.')

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    @property
    def action_chains(self):
        return ActionChains(self.driver)

    def scroll_to(self, element):
        self.driver.execute_script('arguments[0].scrollIntoView(true);', element)


    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def search(self, query):
        search = self.find(self.locators.QUERY_LOCATOR)
        search.clear()
        search.send_keys(query)
        go_button = self.find(self.locators.GO_LOCATOR)
        go_button.click()

    def click(self, locator, timeout=None):
        self.logger.info(f'Clicking on a locator {locator}')
        for i in range(CLICK_RETRY):
            try:
                elem = self.find(locator, timeout=timeout)
                elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                elem.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise
