from ui.pages.base_page import BasePage
from ui.locators.basic_locators import EventPageLocators

class EventsPage(BasePage):
    url = 'https://www.python.org/events/python-events/past/'
    locators = EventPageLocators()


    def get_location(self):
        return self.find(self.locators.EVENT_LOCATION).text