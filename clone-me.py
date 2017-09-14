#!/usr/bin/env python

import sys
import os
import subprocess

clone_to = sys.argv[1]

cwd = os.getcwd()
os.mkdir('../%s' % (clone_to,))
os.mkdir('../%s/%s' % (clone_to, clone_to))
for fn in ['setup.py', 'README', 'anisble/__init__.py']:
  ofs = open('../%s/%s' % (clone_to, fn.replace('anisble', clone_to)), 'w')
  ofs.write(open(fn).read().replace('anisble', clone_to))
  ofs.close()
os.chdir('../%s' % (clone_to,))
try:
  subprocess.check_call(['python', 'setup.py', 'sdist', 'upload'])
finally:
  os.chdir(cwd)
