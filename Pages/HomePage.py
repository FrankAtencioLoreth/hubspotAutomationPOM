from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Config.Locators import Locators

class HomePage(BasePage):
    """By locators"""
    HEADER = (By.CSS_SELECTOR, Locators.HEADER_CSS)
    ACCOUNT_NAME_XPATH = (By.CSS_SELECTOR, Locators.ACCOUNT_NAME_XPATH)
    NAVIGATION_SETTING_LINK = (By.ID, Locators.NAVIGATION_SETTING_LINK)
    GOTODASHBOARD_XPATH = (By.XPATH, Locators.GOTODASHBOARD_XPATH)
    REPORTS_MENU_LINK = (By.ID, Locators.REPORTS_MENU_LINK)
    ITEM_REPORTS_MENU_LINK = (By.ID, Locators.ITEM_REPORTS_MENU_LINK)

    """Constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Page actions for Login page"""
    def gotoDashBoard(self):
        self.doClick(self.REPORTS_MENU_LINK)
        self.doClick(self.ITEM_REPORTS_MENU_LINK)

    def getHomePageTitle(self, title):
        return self.getTitle(title)

    def isSettingIconExist(self):
        return self.isVisible(self.NAVIGATION_SETTING_LINK)

    def getHeaderValue(self):
        if self.isVisible(self.HEADER):
            return self.getElementText(self.HEADER)

    def getAccountNameValue(self):
        if self.isVisible(self.ACCOUNT_NAME_XPATH):
            return self.getElementText(self.ACCOUNT_NAME_XPATH)