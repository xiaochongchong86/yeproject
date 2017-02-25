# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest

class BugfreeNewbug(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/"
    
    def test_bugfree_newbug(self):
        driver = self.driver
        driver.get(self.base_url + "bugfree/index.php/site/login")
        driver.find_element_by_id("LoginForm_username").clear()
        driver.find_element_by_id("LoginForm_username").send_keys("admin")
        driver.find_element_by_id("LoginForm_password").clear()
        driver.find_element_by_id("LoginForm_password").send_keys("123456")
        driver.find_element_by_id("SubmitLoginBTN").click()
        driver.find_element_by_link_text(u" 新建 Bug   ").click()
        self.assertEqual(u"                 新建Bug            " , driver.find_element_by_id("span_info_id").text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
