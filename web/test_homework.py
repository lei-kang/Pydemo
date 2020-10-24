from time import sleep

from selenium import webdriver
import shelve
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class Test_Homework():
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def teardown_class(self):
        sleep(5)
        self.driver.quit()

    def test_login(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        db = shelve.open('cookies')
        cookies = db['cookies']
        db.close()
        for cookie in cookies:
            self.driver.add_cookie(cookie)

        self.driver.refresh()
        ele = self.driver.find_element(By.CSS_SELECTOR,"#menu_index span").get_attribute("innerHTML")
        assert ele == '首页'

    def test_join(self):
        self.driver.find_element(By.CSS_SELECTOR,".index_service_cnt_itemWrap:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_uploadInputMask").send_keys("D:\\123.xlsx")
        name = self.driver.find_element(By.CSS_SELECTOR,".ww_fileImporter_fileContainer_fileNames").text
        assert name == '123.xlsx'

    def test_join_2(self):
        self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_submitWrap").click()
        # WebDriverWait(self.driver,10).until(expected_conditions.visibilty_of(self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_failInfo")))
        ele = self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_failInfo").text
        print(ele)
        assert ele == "失败1人"

