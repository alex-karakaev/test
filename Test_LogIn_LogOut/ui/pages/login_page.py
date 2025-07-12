from selenium.webdriver.support.wait import WebDriverWait
from ui.pages.base_page import BasePage
from ui.locators.basic_locators import LoginPageLocators
from selenium.webdriver.support import expected_conditions as EC
from ui.locators import basic_locators


class LoginPage(BasePage):

    def login(self, user, password):
        cookies_button = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(basic_locators.BasePageLocators.COOKIES_SUBMIT_BUTTON_LOCATOR)
        )
        cookies_button.click()

        self.click(basic_locators.DashBoardLocators.LOGIN_LOCATOR)
        self.find(basic_locators.LoginPageLocators.LOGIN_LINE_LOCATOR).send_keys(user)
        self.find(basic_locators.LoginPageLocators.PASSWORD_LINE_LOCATOR).send_keys(password)

        self.click(basic_locators.LoginPageLocators.SUBMIT_BUTTON_LOCATOR)




