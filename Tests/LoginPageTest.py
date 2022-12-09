from Pages.LoginPage import LoginPage
from Tests.BaseTest import BaseTest
from Config.TestData import TestData


class TestLoginPage(BaseTest):

    # console command pytest Tests/LoginPageTest.py (normal)
    # pip install pytest-html
    # console command pytest Tests/LoginPageTest.py -v --html=reports/report.html (with report)

    def test_sigup_link_visible(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.isSingupLinkExist()
        assert flag

    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.getTitle(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.doLogin(TestData.USER_NAME, TestData.PASSWORD)
