#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""
# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(dir):
  filenames = os.listdir(dir)
  s=' '
  paths=[]
  fnspecial = re.findall(r'\w+__\w+__.\w+', s.join(filenames))
  for filename in fnspecial:
    path=os.path.join(dir, filename)
    paths.append(path)
  return paths 

def print_special_paths(dir):
  paths=get_special_paths(dir)
  for path in paths:
    print os.path.abspath(path)
  return 

def copy_to(paths, dir):
  d = get_special_paths(dir)
  if not os.path.exists(paths):
    os.mkdir(paths)
  for dir in d:
    shutil.copy(dir, paths)
  return

def zip_to(dir, zippath):
  d = get_special_paths(dir)
  cmd = 'zip ' + zippath
  for i in d:
    cmd= cmd + ' ' + i
  (status, output) = commands.getstatusoutput(cmd)
  print output
  return



def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]
  
  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  for dir in args:
    get_special_paths(dir)
    if tozip:
      zip_to(dir, tozip)
    elif todir:
      copy_to(todir, dir)
      print 'written to dir', todir
    else: print_special_paths(dir)
  # Call your functions
  
if __name__ == "__main__":
  main()
