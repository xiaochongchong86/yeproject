#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest
from selenium import webdriver


class BaiduSearchTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com"

    def test_handle_windows(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").click()
        driver.find_element_by_id("kw").send_keys(u"虎门镇")
        driver.find_element_by_id("su").click()

        driver.find_element_by_link_text(u"虎门镇_百度百科").click()
        win_list = driver.window_handles
        print driver.window_handles
        print driver.current_window_handle
        driver.switch_to.window(win_list[1])
        print driver.current_window_handle
        print driver.current_url


if __name__ == "__main__":
    unittest.main()