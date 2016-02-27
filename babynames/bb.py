#!/usr/bin/python

import re
import sys
##lst=[]
d={}

f=open('baby1992.html', 'rU')
year=re.search(r'<h3 align="center">Popularity in ([\d]+)</h3>', f.read())
f.close()
d[year.group(1)]=''
##lst.append(year.group(1))


f=open('baby1992.html', 'rU')
names=re.findall(r'<tr align="right"><td>([\d]+)</td><td>([\w]+)</td><td>([\w]+)</td>', f.read())
f.close()
for n in names:
  d[n[1]]=n[0]
  d[n[2]]=n[0]

##print lst
for key in sorted(d.keys()):
  print key, d[key]



