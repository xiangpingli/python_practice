#!/usr/bin/python


def list_test():
  list_test=["hikvision", 'dahua', 'huawei', 'h3c', 'alibaba']
  print list_test
  
  list_test.append('nokia')
  print list_test 

  list_test.remove('dahua')
  print list_test

  print list_test[1:]

  print list_test[:2]

  list_new = ["baidu", "sina", "360"]
  
  print list_test + list_new
  
  list_all = list_test + list_new

  print list_all

  for t in list_all:
    print t

  print "\n"

  for t in sorted(list_all):
    print t

  print dir(list_test)

if __name__=="__main__":
  list_test()
