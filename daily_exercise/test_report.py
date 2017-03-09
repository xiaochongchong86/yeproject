#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import unittest
from HTMLTestRunner import HTMLTestRunner


class TestMountain(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_ti_is_true(self):
        self.assertTrue(1 != 0)
        print "fail..."

    def test_it_is_false(self):
        self.assertFalse(0 == 1)
        print "seccess..."

    def test_strip_quote_strings(self):
        self.assertTrue('aaa' == "aaa")

    def test_strip_strings(self):
        self.assertTrue("   aa   ".strip() == "aa")
        self.assertTrue("  a".lstrip() == "a")
        self.assertTrue("aa   ".rstrip() == "aa")


def fun_suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(TestMountain))
    return suite

if __name__ == '__main__':

    fp = open('./test_result_%s.html' % time.strftime("%Y-%m-%d %H-%M-%S"),'wb')
    runner = HTMLTestRunner(stream=fp,
                            title=u"测试报告",
                            description=u"测试用例执行情况: ")
    runner.run(fun_suite())
    fp.close()
    sys.exit(0)
