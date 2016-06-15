#!/usr/bin/python


def dict_test():

  dict_test={'hangzhou':'hikvision', 'shenzhen':'huawei', 'beijing':'baidu'}
  print dict_test
 
  for key in dict_test.keys():
    print "key=%s, value=%s" %(key, dict_test[key])  

  for key in dict_test:
    print "key=%s, value=%s" %(key, dict_test[key])

  dict_new = dict_test.copy()
  print dict_new
  print "len(dict_new):%d" %len(dict_new)

  dict_get = dict(American='Newyork', China='Beijing')
  print dict_get
  print dict_get.keys()
  print dict_get.values()
  print dict_get.items()
  
  for item in dict_get.items():
    print item


  dict_test.update(dict_get)
  print dict_test

if __name__=='__main__':

  dict_test()
