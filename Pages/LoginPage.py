from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Config.Locators import Locators

class LoginPage(BasePage):

    """By locators"""
    EMAIL = (By.ID, Locators.EMAIL_INPUT)
    PASSWORD = (By.ID, Locators.PASSWORD_INPUT)
    LOGIN_BUTTON = (By.ID, Locators.LOGIN_BUTTON)
    SIGN_UP_LINK = (By.LINK_TEXT, Locators.SIGNUP_LINK)

    """Constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Page actions for Login page"""
    def getTitleLoginPage(self ,title):
        return self.getTitle(title)

    def isSingupLinkExist(self):
        return self.isVisible(self.SIGN_UP_LINK)

    def doLogin(self, username, password):
        self.dosendKeys(self.EMAIL, username)
        self.dosendKeys(self.PASSWORD, password)
        self.doClick(self.LOGIN_BUTTON)

