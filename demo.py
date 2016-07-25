#!/usr/bin/env python
# -*- coding: utf-8 -*-

from email_proxy import email_proxy

def main():
    ep = email_proxy.email_proxy('smtp.126.com', 'username', 'password')
    print ep.send(['xxxx@xxx.com'], 'this is subject', 'this is body')
    return

if __name__ == '__main__':
    main()
