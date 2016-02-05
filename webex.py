#!/usr/bin/env python3
 
# The above line is not necessary for Windows, because paths are configured globally...

import subprocess

crazy_variable = 1

sane_variable = 2

if crazy_variable == sane_variable:
    print ('hello world')
else:
    print ('thats crazy talk')


if 5*5 == 25: 
    print ('this is NOT crazy talk')
else: 
    print ('thats crazy talk')
