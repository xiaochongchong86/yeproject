# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest

class BugfreeLoginLogout(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/"
    
    def test_bugfree_login_and_logout(self):
        """成功登陆并退出"""
        driver = self.driver
        driver.get(self.base_url + "bugfree/index.php/site/login")
        self.assertEqual(u"登录 - BugFree",driver.title)
        driver.find_element_by_id("LoginForm_username").clear()
        driver.find_element_by_id("LoginForm_username").send_keys("admin")
        driver.find_element_by_id("LoginForm_password").clear()
        driver.find_element_by_id("LoginForm_password").send_keys("123456")
        driver.find_element_by_id("SubmitLoginBTN").click()
        self.assertEqual("BugFree", driver.title)
        driver.find_element_by_link_text(u"退出").click()
        self.assertEqual(u"登录 - BugFree", driver.title)

    def test_bugfree_username_empty(self):
        """用户名为空登陆"""
        driver = self.driver
        driver.get(self.base_url + "bugfree/index.php/site/login")
        self.assertEqual(u"登录 - BugFree", driver.title)
        driver.find_element_by_id("LoginForm_username").clear()
        driver.find_element_by_id("LoginForm_username").send_keys("")
        driver.find_element_by_id("LoginForm_password").clear()
        driver.find_element_by_id("LoginForm_password").send_keys("123456")
        driver.find_element_by_id("SubmitLoginBTN").click()
        self.assertEqual(u"用户名 不可为空白.  ", driver.find_element_by_id("login-error-div").text)

    def test_bugfree_password_empty(self):
        """密码为空登陆"""
        driver = self.driver
        driver.get(self.base_url + "bugfree/index.php/site/login")
        self.assertEqual(u"登录 - BugFree", driver.title)
        driver.find_element_by_id("LoginForm_username").clear()
        driver.find_element_by_id("LoginForm_username").send_keys("admin")
        driver.find_element_by_id("LoginForm_password").clear()
        driver.find_element_by_id("LoginForm_password").send_keys("")
        driver.find_element_by_id("SubmitLoginBTN").click()
        self.assertEqual(u"密码 不可为空白.  ", driver.find_element_by_id("login-error-div").text )

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
