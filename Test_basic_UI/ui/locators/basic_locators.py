from selenium.webdriver.common.by import By


class BasePageLocators:
    QUERY_LOCATOR = (By.ID, 'id-search-field')
    GO_LOCATOR = (By.XPATH, "//button[contains(@class, 'search-button')]")
    #GO_LOCATOR = (By.XPATH, "//*[@class='search-button']")
    ABOUT_LOCATOR = (By.ID, 'about')
    DOWNLOADS_LOCATOR = (By.ID, 'downloads')
    DOCUMENTATION_LOCATOR = (By.ID, 'documentation')

    LOGIN_LOCATOR = (By.XPATH, '//a[@href="/login"]')
    COOKIES_SUBMIT_BUTTON_LOCATOR = (By.XPATH, '//button[contains(@class, "fc-cta-consent")]')
    CART_LOCATOR = (By.XPATH, '//a[@href="/view_cart"]')


class MainPageLocators:
    COMPREHENSIONS = (By.XPATH, "//code/span[@class='comment' and contains(text(), 'comprehensions')]") #works only for python.org
    EVENTS_BUTTON = (By.XPATH, "//li[@id='events']/a[@href='/events/']")
    EVENTS_BUTTON_TEMPLATE = (By.XPATH, "//li[@id='events']//a[@href='/events/{}/']")
    INTRODUCTION = (By.CSS_SELECTOR, "div.introduction")
    LEARN_MORE_RELATIVE = (By.CSS_SELECTOR, "a.readmore")

    START_SHELL = (By.ID, 'start-shell')
    PYTHON_CONSOLE = (By.ID, 'hterm:row-nodes')

    CONSOLE_IFRAME = (By.XPATH, '//iframe[@src="https://console.python.org/python-dot-org-console/"]')
    INPUT_IFRAME = (By.ID, 'id_console')

    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "add-to-cart")
    DRESS_ADD_BUTTON = (By.ID, "3")

class LoginPageLocators(BasePageLocators):
    LOGIN_LINE_LOCATOR = (By.XPATH, '//input[@type="email"]')
    PASSWORD_LINE_LOCATOR = (By.XPATH, '//input[@type="password"]')
    SUBMIT_BUTTON_LOCATOR = (By.XPATH, '//button[@class="btn btn-default"]')

class SearchPageLocators(BasePageLocators):
    #NO_RESULTS_FOUND = (By.XPATH, '//p[contains(text(), "No results found.")]')
    NO_RESULTS_FOUND = ((By.XPATH, "//*[@class='list-recent-events menu']"))

class EventPageLocators(BasePageLocators):
    PYCON_LONDON2025 = (By.XPATH, "//a[@href='/events/python-events/2012/']")
    EVENT_LOCATION = (By.CLASS_NAME, 'single-event-location')

class DownloadUploadPage(BasePageLocators):
    DOWNLOAD_FILE_LOCATOR = (By.XPATH, '//a[contains(@href, "https://www.python.org/ftp/python/2.7.17/python2717.chm")]')
    UPLOAD_FILE_LOCATOR = (By.NAME, 'userfile')

class CartPageLocators(BasePageLocators):
    VIEW_CART_BUTTON = (By.XPATH, '//a[@href="/view_cart"]')
    MAN_TSHIRT_LOCATOR = (By.XPATH, '//a[@href="/product_details/2"]')

