#!/usr/bin/env python
# encoding:utf-8
"""
功能：发送纯文本的邮件内容
演示：jupyter notebook 通过SMTP协议发送邮件
使用163邮箱作为测试：
用户名：2915874926@qq.com
密码：qwer1234@@@@
第三方授权码：qwer1234
"""
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def send_email(FROM_ADDR, FROM_PSWD, TO_ADDR, subject,  filepath, mode="html"):
    html_data = ""

    SMTP_SERVER = u"smtp.163.com"

    if not filepath:
        return
    with open(filepath) as fp:
        html_data = fp.read()
    msg = MIMEText(html_data, 'html', 'utf-8')
    msg['From'] = _format_addr(u'Python爱好者 <%s>' % FROM_ADDR)
    msg['To'] = _format_addr(u'管理员 <%s>' % TO_ADDR)
    msg['Subject'] = Header(subject, 'utf-8').encode()

    server = smtplib.SMTP(SMTP_SERVER)
    server.login(FROM_ADDR, FROM_PSWD)
    server.sendmail(FROM_ADDR, [TO_ADDR], msg.as_string())
    server.quit()

if __name__ == "__main__":
    send_email()