from ui.pages.base_page import BasePage
from ui.locators.basic_locators import MainPageLocators
from ui.pages.event_page import EventsPage


class MainPage(BasePage):

    locators = MainPageLocators()

    def go_to_events(self, event):
        events_button = self.find(self.locators.EVENTS_BUTTON)
        self.action_chains.move_to_element(events_button).perform()
        event_locator = (self.locators.EVENTS_BUTTON_TEMPLATE[0],
                         self.locators.EVENTS_BUTTON_TEMPLATE[1].format(event)
                         )
        self.click(event_locator)
        return EventsPage(self.driver)

