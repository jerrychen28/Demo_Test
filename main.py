# coding=utf-8

import unittest
import time
import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import os


def add_case(case_path, rule):
    """Add all the test cases"""
    testunit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_path, pattern=rule, top_level_dir=None)
    testunit.addTests(discover)
    return testunit

def run_case(all_case, report_path):
    """Exection of all test cases, using HTML style test report"""
    now = time.strftime("%Y_%m_%d %H_%M_%S")
    report_abspath = os.path.join(report_path, now + "result.html")
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Automation Test Report', description='Results of Test Case Execution')
    runner.run(all_case)
    fp.close()

def get_report_file(report_path):
    """Get the latest test report"""
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
    report_file = os.path.join(report_path, lists[-1])
    return report_file

def send_mail(sender, psw, receiver, smtpserver, report_file):
    """Send the latest test report content"""
    with open(report_file, "rb") as f:
        mail_body = f.read()
    msg = MIMEMultipart()
    body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    msg['Subject'] = "Automation Test Report"
    msg["from"] = sender
    msg["to"] = ";".join(receiver)
    msg.attach(body)
    att = MIMEText(open(report_file, "rb").read(), "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename= "report.html"'
    msg.attach(att)
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(sender, psw)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()

if __name__ == "__main__":
    case_path = os.path.join(os.getcwd(), "testsuite")
    rule = "test*.py"
    all_case = add_case(case_path, rule)
    report_path = os.path.join(os.getcwd(), "testreport")
    run_case(all_case, report_path)
    report_file = get_report_file(report_path)
    sender = "398129708@qq.com"
    This is not a correct password
    psw = "123456"
    receiver = ["jerry.xin.chen1@gmail.com", "jerrychen28@163.com"]
    smtp_server = 'smtp.exmail.qq.com'
    send_mail(sender, psw, receiver, smtp_server, report_file)