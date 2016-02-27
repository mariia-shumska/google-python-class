#!/usr/bin/python -tt

import sys

f = open(sys.argv[1], 'rU')
text=f.read()
lst=text.lower().split()
d = {}
i=1
count=1
while lst:
  if i<len(lst) and lst[0]==lst[i]:
    del lst[i]
    count+=1
  else:
    i+=1
    if i>=len(lst):
      d[lst[0]]=count
      del lst[0]
      i=1
      count=1

def sss(s): return s[-1]
for k,v in sorted(d.items(), key=sss, reverse=True):
  print k, v
  
##for k, v in d.items(): print k, '>', v
#for v in sorted(d.values()):
#  print v, d[v]


   
f.close()
