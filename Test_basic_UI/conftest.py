import logging
import os.path
import shutil
import pytest
from selenium import webdriver
from ui.fixtures import *
from test_login import LoginPage

def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--url', default='https://www.python.org/')
    parser.addoption('--debug_log', action='store_true')


@pytest.fixture(scope='session')
def config(request):
    browser = request.config.getoption('--browser')
    url = request.config.getoption('--url')
    debug_log = request.config.getoption('--debug_log')

    return {'browser': browser, 'url': url, 'debug_log': debug_log}

@pytest.fixture(scope='function')
def logger(temp_dir, config):
    log_formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
    log_file = os.path.join(temp_dir, 'test.log')
    log_level = logging.DEBUG if config['debug_log'] else logging.INFO

    file_handler = logging.FileHandler(log_file, 'w')
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(log_level)

    log = logging.getLogger('test')
    log.propagate = False
    log.setLevel(log_level)
    log.handlers.clear()
    log.addHandler(file_handler)

    yield log

    for handler in log.handlers:
        handler.close()


@pytest.fixture(scope='session')
def base_temp_dir():
    base_dir = r'C:\pythonProject\downloads'

    if os.path.exists(base_dir):
        try:
            shutil.rmtree(base_dir)
        except Exception as exc:
            print(f'Couldnt delete catalogue: {exc}')

    os.makedirs(base_dir)
    return base_dir


@pytest.fixture(scope="function")
def temp_dir(base_temp_dir, request):
    test_dir = os.path.join(base_temp_dir, request.node.nodeid.replace(':', '_'))
    os.makedirs(test_dir)
    return test_dir


@pytest.fixture(scope='session')
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.path.pardir))


@pytest.fixture(scope='session')
def cookies(credentials, config):
    driver = get_driver(config["browser"])
    driver.get(config["url"])
    login_page = LoginPage(driver)
    login_page.login(*credentials)

    cookie = driver.get_cookies()
    driver.quit()
    return cookie

