from ui.pages.base_page import BasePage
from ui.locators import basic_locators
from ui.locators.basic_locators import CartPageLocators
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException


class CartPage(BasePage):
    locators = CartPageLocators

    def cart_check(self):
        self.find(basic_locators.MainPageLocators.DRESS_ADD_BUTTON)
        self.click(basic_locators.MainPageLocators.DRESS_ADD_BUTTON)
        cart_button = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(basic_locators.CartPageLocators.VIEW_CART_BUTTON)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", cart_button)
        cart_button.click()

    def cart_delete(self):
        self.click(basic_locators.CartPageLocators.VIEW_CART_BUTTON)
        while True:
            delete_buttons = self.driver.find_elements(*basic_locators.CartPageLocators.DELETE_BUTTON)

            if not delete_buttons:
                assert "Cart is empty!" in self.driver.page_source
                break

            delete_buttons[0].click()
            time.sleep(1.5)
