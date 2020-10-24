from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import shelve
class Test_Case():

    def setup_method(self,method):
        options=Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)

    def teardown_method(self,method):
        self.driver.quit()


    def test_case(self):

        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        self.driver.refresh()

    def test_cookies(self):
        cookies = self.driver.get_cookies()
        print(cookies)
        db = shelve.open("cookies")
        db["cookies"] = cookies
        db.close()

