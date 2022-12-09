import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeService
from selenium.webdriver.firefox.service import Service as firefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(params=["chrome"], scope="class")
def init_driver(request):
    web_driver = None
    if request.param == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        web_driver = webdriver.Chrome(service=chromeService(ChromeDriverManager().install()), options=chrome_options)
    if request.param == "firefox":
        web_driver = webdriver.Firefox(service=firefoxService(GeckoDriverManager().install()))
    request.cls.driver = web_driver
    web_driver.maximize_window()
    web_driver.implicitly_wait(30)
    yield
    web_driver.close()

