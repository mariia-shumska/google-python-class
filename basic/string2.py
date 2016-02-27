#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
  # +++your code here+++
  ## if len(s) >=3: return s[0:] + 'ing'
  ## if s[-3:] = 'ing': return s[0:] + 'ly'
  ##else: return s[0:]
  if  len(s) >=3 and s[-3:] == 'ing': return s[0:] + 'ly'
  else:
   if len(s) >=3: return s[0:] + 'ing'
   else: return s

 


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
 ## if s=='not' and s=='bad':
 ## return s[:'not'] + 'good'
  a=s.find('not')
  b=s.find('bad')
  if 0<a<b:
   s=s.replace(s[a:b+3],'good')
 ## else: s=s
  return s

# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
  
 
#  if (len(a)==2 or len(a)==4 or len(a)==6 or len(a)==8) and (len(b)==2 or len(b)==4 or len(b)==6 or len(b)==8):
#   ha=len(a)/2
#   hb=len(b)/2
#   return a[0:ha] + b[0:hb] + a[ha:] + b[hb:]
#
#  if (len(a)==3 or len(a)==5 or len(a)==7 or len(a)==9) and (len(b)==2 or len(b)==4 or len(b)==6 or len(b)==8):
#   ha=len(a)/2
#   hb=len(b)/2
#   return a[0:ha+1] + b[0:hb] + a[ha+1:] + b[hb:] 
#   
#  if (len(a)==3 or len(a)==5 or len(a)==7 or len(a)==9) and (len(b)==3 or len(b)==5 or len(b)==7 or len(b)==9):
#   ha=len(a)/2
#   hb=len(b)/2
#   return a[0:ha+1] + b[0:hb+1] + a[ha+1:] + b[hb+1:]
#
#  if (len(a)==2 or len(a)==4 or len(a)==6 or len(a)==8) and (len(b)==3 or len(b)==5 or len(b)==7 or len(b)==9):
#   ha=len(a)/2
#   hb=len(b)/2
#   return a[0:ha] + b[0:hb+1] + a[ha:] + b[hb+1:]

# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print 'verbing'
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print
  print 'not_bad'
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print
  print 'front_back'
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()
