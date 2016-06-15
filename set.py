#!/usr/bin/python


def set_test():
  set_test = set('hikvision')
  print set_test

  for k in set_test:
    print k  

   
  set_new = set(["hello", "world"]) 
  print set_new
  for k in set_new:
    print k

  set_new.add("hikvision")
  for k in set_new:
    print k

  set_new.update(["good"])
  for k in set_new:
    print k


if __name__=="__main__":
  set_test()
