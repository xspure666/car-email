# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os


def send(content, zipFile):
    fromaddr = 'lumingtong@kmcharge.com'
    password = 'Lmt@789'
    toaddrs = ['fanghuanhua@kmcharge.com', 'lumingtong@kmcharge.com']

    textApart = MIMEText(content)

    # imageFile = '1.png'
    # imageApart = MIMEImage(open(imageFile, 'rb').read(), imageFile.split('.')[-1])
    # imageApart.add_header('Content-Disposition', 'attachment', filename=imageFile)

    # pdfFile = r'C:\Users\Galen\Documents\nginx\appapitest.kmcharge.com.access.log-20200722.gz'
    # pdfApart = MIMEApplication(open(pdfFile, 'rb').read())
    # pdfApart.add_header('Content-Disposition', 'attachment', filename=pdfFile)
    # zipFile = r'warning_car.tar.gz'
    zipApart = MIMEApplication(open(zipFile, 'rb').read())
    zipApart.add_header('Content-Disposition', 'attachment', filename=zipFile)

    m = MIMEMultipart()
    # attach(MIMEText('这是菜鸟教程Python 邮件发送测试……', 'plain', 'utf-8'))
    m.attach(MIMEText(content))
    # # m.attach(imageApart)
    # m.attach(pdfApart)
    m.attach(zipApart)
    m['Subject'] = '车平台每周告警数据自动推送'
    m['From'] = 'lumingtong@kmcharge.com'
    m['to'] = 'fanghuanhua@kmcharge.com,lumingtong@kmcharge.com'

    try:
        print("正在发送邮件...............")
        server = smtplib.SMTP("imap.exmail.qq.com")
        server.login(fromaddr, password)
        server.sendmail(fromaddr, toaddrs, m.as_string())
        print('邮件发送.........success')
        server.quit()
    except smtplib.SMTPException as e:
        print('error:', e)  # 打印错误
