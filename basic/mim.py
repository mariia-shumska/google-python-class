#!/usr/bin/python -tt

import sys
import random

f=open('test.txt', 'rU')
text=f.read().split()
print text

dict={}
i=0
while i< len(text):
  if text[i] not in dict: 
    dict[text[i]]=text[i+1:]
    i+=1
  else : i+=1
for k in dict:
  print k,':', dict[k]
