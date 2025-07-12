from ui.pages.base_page import BasePage
from ui.locators.basic_locators import DashBoardLocators


class DashboardPage(BasePage):

    def log_out(self):
        self.click(DashBoardLocators.LOGOUT_BUTTON_LOCATOR)