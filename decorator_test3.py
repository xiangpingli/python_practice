#!/usr/bin/python


def deco1(func):
  def _deco1():
    print 'enter deco1 called'
    func()
    print 'leave deco1 called'
  return _deco1
   
@deco1
def decorator_test():
  print 'decorator_test is called'

if __name__=="__main__":
    decorator_test()
