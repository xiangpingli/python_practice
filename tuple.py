#!/usr/bin/python

def tuple_test():
  tuple_test = ('hikvision', 'dahua', 'huawei', 'alibaba')
  print tuple_test

  print tuple_test[1:]

  print tuple_test[:2]

  for t in tuple_test:
    print t

  tuple_new = ('baidu', 'sina', 'netease')

  print tuple_new

  tuple_all = tuple_test + tuple_new

  print tuple_all

  (tuple_a, tuple_b) = (tuple_test, tuple_new)
  print tuple_a
  print tuple_b

if __name__=="__main__":
  tuple_test()
