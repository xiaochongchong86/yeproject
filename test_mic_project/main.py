#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import logging
import unittest
from lib.Logger import Logger
from lib.HTMLTestRunner import HTMLTestRunner
from testcase.admin_login_logout.admin_login_correction import AdminLoginCorrection
from lib.SendEmail import send_email

FROM_ADDR = u"qq2915874926@163.com"
FROM_PSWD = u"qwer1234"  # 163设置的第三方授权码
TO_ADDR = u"qq2915874926@163.com"


def suites():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(AdminLoginCorrection))
    return suite

if __name__ == "__main__":
    logger = Logger().getlog()
    logger.info('start testcase...')
    report_path = 'result/test_result_%s.html' % time.strftime("%Y-%m-%d %H-%M-%S")

    fp = open(report_path,'wb')
    runner = HTMLTestRunner(stream=fp,
                            title=u"测试报告",
                            description=u"测试用例执行情况: ")
    runner.run(suites())
    fp.close()
    send_email(FROM_ADDR, FROM_PSWD, TO_ADDR, u"测试报告", report_path)

    logger.info('stop testcase...')