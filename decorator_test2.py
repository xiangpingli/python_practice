#!/usr/bin/python


def deco1(func):
  print 'enter deco1 called'
  func()
  print 'leave deco1 called'
  return func
   
@deco1
def decorator_test():
  print 'decorator_test is called'

if __name__=="__main__":
    decorator_test()
