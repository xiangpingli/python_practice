#!/usr/bin/python

import os


def dir_test_main():
  print "I AM @ dir_test_main()"
  
  cwd = os.getcwd()
  print cwd

  file_list = os.listdir(cwd)
  print file_list

  for file_name in file_list:
    print file_name

if __name__ == "__main__":
  dir_test_main()

