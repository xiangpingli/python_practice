#!/usr/bin/python

import string

def string_test():
  str1 = "hello"
  str2 = "world"
  
  print len(str1)
  print str1[:2]
  print str1[1:]

  ret = 'bc' in str1
  print ret

  ret = 'he' in str1
  print ret

  ret = 'bc' not in str1
  print ret 

  print string.lowercase

  print string.digits

  print string.letters

  print string.uppercase

  
  
  str_input=raw_input("Input a string:")
  print("Your input:%s" % str_input)

  str3 = str1 + " " + str2
  print("str3:%s" % str3)


  str4 = "%s %s" % (str1, str2)
  print("str4:%s" % str4)

  str5 = ' '.join((str1, str2))
  print("str5:%s" % str5)

  str6 = ','.join((str1, str2))
  print("str6:%s" % str6)


if __name__=="__main__":
  string_test()
