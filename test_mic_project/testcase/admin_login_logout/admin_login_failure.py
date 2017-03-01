#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coder: samren
# version : 1.0
import unittest
from selenium import webdriver


class AdminLoginFail(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/"

    def test_admin_login_failure_with_wrong_username(self):
        """测试不正确的admin用户名"""
        driver = self.driver
        driver.get(self.base_url + "bugfree/index.php/site/login")
        self.assertEqual(u"登录 - BugFree", driver.title)
        driver.find_element_by_id("LoginForm_username").clear()
        driver.find_element_by_id("LoginForm_username").send_keys("adminn")
        driver.find_element_by_id("LoginForm_password").clear()
        driver.find_element_by_id("LoginForm_password").send_keys("123456")
        driver.find_element_by_id("SubmitLoginBTN").click()
        self.assertEqual(u"用户名不存在 ", driver.find_element_by_id("login-error-div").text)

    def test_admin_login_failure_with_wrong_password(self):
        """测试不正确的admin密码"""
        driver = self.driver
        driver.get(self.base_url + "bugfree/index.php/site/login")
        self.assertEqual(u"登录 - BugFree", driver.title)
        driver.find_element_by_id("LoginForm_username").clear()
        driver.find_element_by_id("LoginForm_username").send_keys("admin")
        driver.find_element_by_id("LoginForm_password").clear()
        driver.find_element_by_id("LoginForm_password").send_keys("12345678")
        driver.find_element_by_id("SubmitLoginBTN").click()
        self.assertEqual(u"用户名和密码不匹配  ", driver.find_element_by_id("login-error-div").text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
