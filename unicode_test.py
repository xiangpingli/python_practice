#!/usr/bin/python
#encoding=utf-8

import sys 
reload(sys) 
sys.setdefaultencoding('utf8')


def unicode_test():
  str1=u"中文"
  print u"%s" % str1

  str2=raw_input("请输入中文：".decode('utf-8').encode('utf-8'))
  print u"%s" % str2

  str3=raw_input(u"请输入中文：")
  print u"%s" % str3

if __name__=="__main__":
  unicode_test()
