from selenium import webdriver
from time import sleep
def demo():
    diver = webdriver.Chrome()
    diver.get('https://myssl.com/aplus.ssldemo.cn?domain=aplus.ssldemo.cn&status=success')
    s = diver.find_element_by_xpath('//*[@id="basic_b"]/div[1]/div/table/tbody/tr[1]/td[2]/p[1]/span[2]').get_attribute("innerHTML")
    diver.implicitly_wait(2)
    print(s)
    sleep(5)

    diver.quit()

if __name__ == '__main__':
    demo()