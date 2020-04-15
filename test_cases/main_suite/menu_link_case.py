from selenium.webdriver.common.by import By
import time
from selenium import webdriver
import os
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

current_path=os.path.dirname(__file__)
print(current_path)
chrome_driver_path=os.path.join(current_path,'../../webdriver/chromedriver')

class MenuLinkCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('http://127.0.0.1:8999/zentao/user-login-L3plbnRhby8=.html')
        self.driver.find_element(By.XPATH, '//input[@id="account"]').send_keys('admin')
        self.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys('Gis123456')
        self.driver.find_element(By.XPATH, '//button[@id="submit"]').click()

    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()

    def test_my_link(self):
        self.driver.find_element(By.XPATH, '//li[@data-id="my"]').click()
        self.assertTrue(WebDriverWait(self.driver, 10).until(EC.title_is("我的地盘 - 禅道")))
    def test_product_link(self):
        self.driver.find_element(By.XPATH, '//li[@data-id="product"]').click()
        self.assertTrue(WebDriverWait(self.driver, 10).until(EC.title_is("产品主页 - 禅道")))
    def test_qa_link(self):
        self.driver.find_element(By.XPATH, '//li[@data-id="qa"]').click()
        self.assertTrue(WebDriverWait(self.driver, 10).until(EC.title_is("测试主页 - 禅道")))
        print('123')
if __name__=='__main__':
    unittest.main()

