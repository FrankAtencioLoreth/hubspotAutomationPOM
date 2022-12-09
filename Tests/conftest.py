import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeService
from selenium.webdriver.firefox.service import Service as firefoxService
from selenium.webdriver.firefox.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(params=["chrome"], scope="class")
def init_driver(request):
    web_driver = None
    if request.param == "chrome":
        web_driver = webdriver.Chrome(service=chromeService(ChromeDriverManager().install()))
    if request.param == "firefox":
        optionsFirefox = Options()
        optionsFirefox.binary_location = r'C:\Program Files\WindowsApps\Mozilla.Firefox_107.0.1.0_x64__n80bbvh6b1yt2\VFS\ProgramFiles\Firefox Package Root\firefox.exe'
        web_driver = webdriver.Firefox(service=firefoxService(GeckoDriverManager().install()), options=optionsFirefox)
    request.cls.driver = web_driver
    web_driver.implicitly_wait(30)
    yield
    web_driver.close()

