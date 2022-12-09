from Pages.LoginPage import LoginPage
from Tests.BaseTest import BaseTest
from Config.TestData import TestData

class TestHomePage(BaseTest):

    # console command pytest Tests/LoginPageTest.py (normal)
    # pip install pytest-html
    # console command pytest Tests/TestLoginPage.py -v --html=reports/report.html (with report)
    def test_home_page_title(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.doLogin(TestData.USER_NAME, TestData.PASSWORD)
        homePage.gotoDashBoard()
        title = homePage.getHomePageTitle(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE

    def test_home_page_header(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.doLogin(TestData.USER_NAME, TestData.PASSWORD)
        homePage.gotoDashBoard()
        header = homePage.getHeaderValue()
        assert header == TestData.HOME_PAGE_HEADER

    def test_home_page_account(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.doLogin(TestData.USER_NAME, TestData.PASSWORD)
        homePage.gotoDashBoard()
        account = homePage.getAccountNameValue()
        assert account == TestData.ACCOUNT_NAME

    def test_seetings_icon(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.doLogin(TestData.USER_NAME, TestData.PASSWORD)
        homePage.gotoDashBoard()
        icon = homePage.isSettingIconExist()
        assert icon