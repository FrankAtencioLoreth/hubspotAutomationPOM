import pytest
from selenium import webdriver
from Config.TestData import TestData

@pytest.fixture(params=["chrome", "firefox"], scope="class")
def init_driver(request):
    web_driver = None
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=TestData.FIREFOX_EXECUTABLE_PATH)
    request.cls.driver = web_driver
    web_driver.implicitly_wait(10)
    yield
    web_driver.close()

