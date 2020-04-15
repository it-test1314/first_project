#登录失败用例
#登录成功的测试用例
import time
import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

current_path=os.path.dirname(__file__)
print(current_path)
chrome_driver_path=os.path.join(current_path,'../../webdriver/chromedriver')

class LoginFailCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=webdriver.Chrome(executable_path=chrome_driver_path)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('http://127.0.0.1:8999/zentao/user-login-L3plbnRhby8=.html')
    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()
    def test_login(self):
        self.driver.find_element(By.XPATH,'//input[@id="account"]').send_keys('admin')
        self.driver.find_element(By.XPATH,'//input[@name="password"]').send_keys('Gis1234561')
        self.driver.find_element(By.XPATH,'//button[@id="submit"]').click()
        self.assertTrue(WebDriverWait(self.driver, 10).until(EC.alert_is_present()))
if __name__=='__main__':
    unittest.main()