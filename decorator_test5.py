#!/usr/bin/python


def deco(func):
  def _deco(*args, **kwargs):
    print("before %s called" % func.__name__)
    ret = func(*args, **kwargs)
    print("after %s called, result:%s" % (func.__name__, ret))
    return ret
  return _deco
   
@deco
def decorator_test(a, b):
  print("decorator_test: (%s, %s)" % (a, b))
  return a+b

@deco
def decorator_test_new(a, b, c):
  print("decorator_test_new: (%s,%s,%s)" %(a,b,c))
  return a+b+c


if __name__=="__main__":
    decorator_test(1, 2)
    decorator_test_new(1, 2, 3)
