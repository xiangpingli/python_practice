#!/usr/bin/python


def deco(func):
  def _deco(a, b):
    print 'before func() called'
    ret = func(a, b)
    print("after func() called, result:%s" % ret)
    return ret
  return _deco
   
@deco
def decorator_test(a, b):
  print("decorator_test: (%s, %s)" % (a, b))
  return a+b

if __name__=="__main__":
    decorator_test(1, 2)
    decorator_test(3, 4)
