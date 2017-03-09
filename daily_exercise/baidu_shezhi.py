#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class FireFox(unittest.TestCase):
    def setUp(self):
        self.drvier = webdriver.Firefox()
        self.drvier.implicitly_wait(30)
        self.base_url = "http://www.baidu.com"

    def tearDown(self):
        self.drvier.quit()

    def test_open_and_search(self):
        dr = self.drvier
        dr.get(self.base_url + "/")
        time.sleep(5)

        link = dr.find_element_by_link_text(u"设置")
        ActionChains(dr).move_to_element(link).perform()
        time.sleep(3)

        dr.find_element_by_link_text(u'搜索设置').click()
        time.sleep(3)

        dr.find_element_by_class_name("prefpanelgo").click()
        time.sleep(3)

        dr.switch_to.alert.accept()
        time.sleep(3)


if __name__ == "__mian__":
    unittest.main()
