import os.path
from contextlib import contextmanager
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base import BaseCase
from ui.locators import basic_locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from ui.utils.decorators import wait


class TestOne(BaseCase):


    @pytest.mark.skip('SKIP')
    def test_title(self):
        assert "Python" in self.driver.title


    @pytest.mark.parametrize(
        'query',
        [
            pytest.param(
                'python'
            ),
            pytest.param(
                'pycon'
            )
        ]
    )

    @pytest.mark.skip("SKIP")
    def test_search(self, query):
        self.base_page.search(query)
        time.sleep(2)
        assert "No results found." not in self.driver.page_source


    @pytest.mark.skip("SKIP")
    def test_negative_search(self):
        self.search_page.search('АБВГДЕЖЗ')
        self.search_page.find(self.search_page.locators.NO_RESULTS_FOUND).is_displayed()

    @pytest.mark.skip("SKIP")
    def test_page_changed(self):
        self.base_page.click(basic_locators.BasePageLocators.GO_LOCATOR)

    @pytest.mark.parametrize(
        'sequence',
        [
            pytest.param(
                basic_locators.BasePageLocators.ABOUT_LOCATOR
            ),
            pytest.param(
                basic_locators.BasePageLocators.DOWNLOADS_LOCATOR
            ),
            pytest.param(
                basic_locators.BasePageLocators.DOCUMENTATION_LOCATOR
            )
        ]
    )

    @pytest.mark.skip("SKIP")
    def test_buttons_press_multiply(self, sequence):
        self.base_page.click(sequence)
        time.sleep(1)

    @pytest.mark.skip("SKIP")
    def test_carousel(self):
        self.base_page.click(basic_locators.MainPageLocators.COMPREHENSIONS, timeout=12)
    #this carousel works only for python.org
    #just wanted to test changing interface on any website

    @pytest.mark.skip("SKIP")
    def test_events(self):
        python_events_page = self.main_page.go_to_events('python-events/past')
        assert python_events_page.is_opened()

    @pytest.mark.skip("SKIP")
    def test_events2(self):
        python_events_page = self.main_page.go_to_events('python-events/past')
        python_events_page.click(python_events_page.locators.PYCON_LONDON2025)
        assert python_events_page.get_location() == 'London, UK'

    @pytest.mark.skip("SKIP")
    def test_relative(self):
        introduction = self.main_page.find(self.main_page.locators.INTRODUCTION)
        learn_more = introduction.find_element(*self.main_page.locators.LEARN_MORE_RELATIVE)
        assert learn_more.get_attribute('href') == self.driver.current_url + 'doc/'


class TestLoad(BaseCase):

    @staticmethod
    def check_download(temp_dir, file_name):
        for f in os.listdir(temp_dir):
            if f.endswith('.crdownload'):
                return False

        assert file_name in os.listdir(temp_dir)
        return True

    #Workds only on Chrome. Anything on Chromium
    @pytest.mark.skip("SKIP")
    def test_download(self, temp_dir):
        self.driver.get('https://www.python.org/downloads/release/python-2717/')

        file_name = "python2717.chm"
        self.main_page.click(basic_locators.DownloadUploadPage.DOWNLOAD_FILE_LOCATOR)

        wait(self.check_download, error=AssertionError, check=True, temp_dir=temp_dir, file_name=file_name)


    @pytest.fixture()
    def file_path(self, repo_root):
        return os.path.join(repo_root, 'files', 'userdata')

    @pytest.mark.skip("SKIP")
    def test_upload(self, file_path):
        self.driver.get('https://ps.uci.edu/~franklin/doc/file_upload.html')

        input_field = self.main_page.find(basic_locators.DownloadUploadPage.UPLOAD_FILE_LOCATOR)
        time.sleep(5)
        input_field.send_keys(file_path)
        time.sleep(5)


class TestInFrame(BaseCase):

    @pytest.mark.skip("SKIP")
    def test_in_frame(self):
        self.main_page.click(self.main_page.locators.START_SHELL)
        time.sleep(12)

        console_iframe = self.main_page.find(self.main_page.locators.CONSOLE_IFRAME)
        self.driver.switch_to.frame(console_iframe)

        input_iframe = self.main_page.find(self.main_page.locators.INPUT_IFRAME)
        self.driver.switch_to.frame(input_iframe)

        iframe = self.main_page.find((By.XPATH, "//iframe"))
        self.driver.switch_to.frame(iframe)

        console = self.main_page.find(self.main_page.locators.PYTHON_CONSOLE)
        console.send_keys('assert 1 == 0')
        console.send_keys(Keys.RETURN)

        time.sleep(10)

        self.driver.switch_to.default_content()


    @contextmanager
    def switch_to_next_window(self, current, close=False):
        for w in self.driver.window_handles:
            if w != current:
                self.driver.switch_to.window(w)
                break
        yield
        if close:
            self.driver.close()
        self.driver.switch_to.window(current)

    @pytest.mark.skip("SKIP")
    def test_new_tabs(self):
        current_window = self.driver.current_window_handle
        events_button = self.main_page.find(self.main_page.locators.EVENTS_BUTTON)
        self.main_page.action_chains\
            .key_down(Keys.CONTROL)\
            .click(events_button)\
            .key_up(Keys.CONTROL)\
            .perform()

        with self.switch_to_next_window(current_window, close=True):
            time.sleep(5)
            assert self.driver.current_url == 'https://www.python.org/events/'

        time.sleep(3)


class TestFailure(BaseCase):

    @pytest.mark.skip("SKIP")
    def test_failure(self):
        self.main_page.find((By.XPATH, '5555ds5dsd4543144587'), timeout=1)

    @pytest.mark.skip("SKIP")
    def test_failure_log(self):
        self.driver.get('https://vk.com/')
        time.sleep(2)
        assert 0


class TestLog(BaseCase):

    def test_log(self):
        self.logger.info('Ready to go to python events')
        python_events_page = self.main_page.go_to_events('python-events/past')

        self.logger.info('Going to PYCON LONDON 2025')
        python_events_page.click(python_events_page.locators.PYCON_LONDON2025)
        location = python_events_page.get_location()
        self.logger.info(f'Get PYCON London 2025 location: {location}')
        assert location == 'London, UK'


@pytest.mark.skip("SKIP")
def test_all_browser(all_drivers):
    time.sleep(1)

