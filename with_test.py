#!/usr/bin/python

def with_test_success():
  with open('with_test.py', 'r') as f:
    for eachline in f:
      print eachline

def with_test_fail():
  with open('not_exist', 'r') as f:
    for eachline in f:
      print eachline
    


if __name__=="__main__":
  
  with_test_success()
  with_test_fail()
