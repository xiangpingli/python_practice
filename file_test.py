#!/usr/bin/python

import os

def file_create():
  f = open("test_file.txt", 'w+')
  f.write("hikvision company!\n")
  f.write("is a great company!\n")
  f.close()


def file_test_main():
  file_create()
  
  f = open("test_file.txt", 'r')
  all_lines = f.readlines()
  f.close()

  for each_line in all_lines:
    print each_line
  
  os.remove('test_file.txt')
  

if __name__=="__main__":
  file_test_main()
