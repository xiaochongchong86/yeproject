#!/usr/bin/env python
# -*- coding: utf-8 -*-


def read_file():
    hfile = open('data.txt','r')
    for i in hfile.readlines():
        print i.strip().decode('gbk')
    hfile.close()

def write_file():
    name_list = [u'张三',u'李四',u'龙五']
    h_file = open('data_write.txt', 'w')
    for i in name_list:
        h_file.write(i.encode('utf-8')+'\n')
    h_file.close()

if __name__ == '__main__':
   # read_file()
    write_file()