#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver

class AdminLoginCorrection(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/"

    def tearDown(self):
        self.driver.quit()

    def test_admin_login(self):
        u"""测试管理员用户是否能成功登录"""
        driver = self.driver
        driver.get(self.base_url + "bugfree/index.php/site/login")
        self.assertEqual(u"登录 - BugFree",driver.title)
        driver.find_element_by_id("LoginForm_username").clear()
        driver.find_element_by_id("LoginForm_username").send_keys("admin")
        driver.find_element_by_id("LoginForm_password").clear()
        driver.find_element_by_id("LoginForm_password").send_keys("123456")
        driver.find_element_by_id("SubmitLoginBTN").click()
        self.assertEqual("BugFree", driver.title)


    def test_admin_logout(self):
        u"""测试管理员退出以后，能否正确跳转"""
        self.assertEqual(2, 2)
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

if __name__ == '__main__':
    unittest.main()