from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""This class is the parent of all pages"""
"""it contains all the generic methods and utilities for all the pages"""

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def doClick(self, byLocator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(byLocator)).click()

    def dosendKeys(self, byLocator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(byLocator)).send_keys(text)

    def getElementText(self, byLocator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(byLocator))
        return element.text

    def isVisible(self, byLocator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(byLocator))
        return bool(element)

    def getTitle(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title