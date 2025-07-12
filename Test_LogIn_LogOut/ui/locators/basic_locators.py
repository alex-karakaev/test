from selenium.webdriver.common.by import By


class BasePageLocators:
    COOKIES_SUBMIT_BUTTON_LOCATOR = (By.XPATH, '//button[contains(@class, "fc-cta-consent")]')


class DashBoardLocators:
    LOGIN_LOCATOR = (By.XPATH, '//a[@href="/login"]')
    CART_LOCATOR = (By.XPATH, '//a[@href="/view_cart"]')
    LOGOUT_BUTTON_LOCATOR = (By.XPATH, '//a[@href="/logout"]')


class MainPageLocators:
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "add-to-cart")
    DRESS_ADD_BUTTON = (By.XPATH, "//a[@data-product-id='3']")


class LoginPageLocators(BasePageLocators):
    LOGIN_LINE_LOCATOR = (By.XPATH, '//input[@type="email"]')
    PASSWORD_LINE_LOCATOR = (By.XPATH, '//input[@type="password"]')
    SUBMIT_BUTTON_LOCATOR = (By.XPATH, '//button[@class="btn btn-default"]')


class CartPageLocators(BasePageLocators):
    VIEW_CART_BUTTON = (By.XPATH, '//a[@href="/view_cart"]')
    PRODUCT_LOCATION = (By.CLASS_NAME, 'cart_description')
    DELETE_BUTTON = (By.XPATH, "//i[contains(@class, 'fa-times')]")

