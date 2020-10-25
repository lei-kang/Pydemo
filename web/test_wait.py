from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Test_Wait():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://ceshiren.com/t/topic/7354")

    def test_wait(self):
        WebDriverWait(self.driver,10).until()
        sleep(3)