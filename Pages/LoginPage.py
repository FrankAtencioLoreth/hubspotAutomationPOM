from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Config.Locators import Locators
from Config.TestData import TestData
from Pages.HomePage import HomePage


class LoginPage(BasePage):

    """By locators"""
    EMAIL = (By.ID, Locators.EMAIL_INPUT)
    PASSWORD = (By.ID, Locators.PASSWORD_INPUT)
    LOGIN_BUTTON = (By.ID, Locators.LOGIN_BUTTON)
    SIGN_UP_LINK = (By.LINK_TEXT, Locators.SIGNUP_LINK)
    MODAL_XPATH = (By.XPATH, Locators.MODAL_XPATH)
    MODAL_BUTTON_XPATH = (By.XPATH, Locators.MODAL_BUTTON_XPATH)

    """Constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.get(TestData.BASE_URL)

    """Page actions for Login page"""
    def getTitleLoginPage(self ,title):
        return self.getTitle(title)

    def isSingupLinkExist(self):
        return self.isVisible(self.SIGN_UP_LINK)

    def doLogin(self, username, password):
        self.dosendKeys(self.EMAIL, username)
        self.dosendKeys(self.PASSWORD, password)
        self.doClick(self.LOGIN_BUTTON)
        if self.isVisible(self.MODAL_XPATH):
            self.doClick(self.MODAL_BUTTON_XPATH)
        return HomePage(self.driver)

