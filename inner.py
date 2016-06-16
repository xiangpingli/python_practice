#!/usr/bin/python

def foo2():
  def bar2():
    print 'bar2() is called'
  print 'foo2() is called'
  bar2()


def foo():
  def bar():
    print 'bar() is called'
  print 'foo() is called'

if __name__=="__main__":
  foo()
  foo2()
