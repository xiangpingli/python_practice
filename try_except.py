#!/usr/bin/python


def try_except_test_with_raise():

  try:
    f = open('not_exist', 'r')

  except IOError, e:
    print 'could not open file:', e
    raise

  print "after try_except"


def try_except_test_no_raise():

  try:
    f = open('not_exist', 'r')

  except IOError, e:
    print 'could not open file:', e

  print "after try_except"

if __name__=="__main__":
  try_except_test_no_raise()
  try_except_test_with_raise()
