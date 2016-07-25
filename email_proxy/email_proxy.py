#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

class email_proxy:
    '''Proxy for send email
    '''

    def __init__(self, smtp_host, user, password, origin = None):
        '''constructor of class email_proxy1
        :param smtp_host: smtp server address, eg: smtp.163.com smtp.126.com smtp.qq.com 192.168.0.1
        :param user: user name(cutoff '@xx.com')
        :param password: password for login user
        :param origin: origin of smtp server(if different from smtp_host, this parameter should be given)
        :return:
        '''
        self.__host = smtp_host
        self.__user = user
        self.__passwd = password
        self.__origin = origin if origin else smtp_host[5:]

    def send(self, to_list, sub, content):
        '''send email
        :param to_list: list of receivers, eg: ['xx@xx.com', 'xx@xx.com']
        :param sub: subject of these mails
        :param content: body of these mails
        :return: True if successfully, False if failed
        '''
        try:
            smtp = smtplib.SMTP(self.__host)
            #smtp.set_debuglevel(1)
            smtp.login(self.__user, self.__passwd)

            from_str = self.__user + '@' + self.__origin
            to_list_str = ';'.join(to_list)
            msg = MIMEText(content, 'plain', 'utf-8')
            msg['Subject'] = Header(sub, 'utf-8')
            msg['From'] = from_str
            msg['To'] = to_list_str

            smtp.sendmail(from_str, to_list_str, msg.as_string())
            return True
        except Exception, e:
            print str(e)
            return False
