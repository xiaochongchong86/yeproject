#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class BaiDuChrome(unittest.TestCase):
    def setUp(self):
        self.executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
        #self.driver = webdriver.Chrome(executable_path=self.executable_path,chrome_options=self.option)
        self.driver = webdriver.Chrome(executable_path=self.executable_path)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)

    def test_open_and_search(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        time.sleep(5)
        driver.find_element_by_name("wd").clear()
        driver.find_element_by_name("wd").send_keys("selenium ide")
        time.sleep(3)
        driver.find_element_by_name("wd").send_keys(Keys.SPACE)
        time.sleep(2)
        driver.find_element_by_name("wd").send_keys(u"教程")

        time.sleep(2)
        driver.find_element_by_name("wd").send_keys(Keys.BACK_SPACE * 2)
        time.sleep(2)
        driver.find_element_by_id("su").click()


if __name__ == "__main__":
    unittest.main()