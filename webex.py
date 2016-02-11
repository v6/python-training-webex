#!/usr/bin/env python3
 
# The above line is not necessary for Windows, because paths are configured globally...

import subprocess

my_command = subprocess.call(['ls', '-a'])

crazy_variable = 10000000

sane_variable = 2

what_to_print = ''

if crazy_variable == sane_variable:
    what_to_print = 'hello world'
else:
    print ('thats crazy talk')


if crazy_variable*crazy_variable == 25: 
    print ('this is NOT crazy talk')
else: 
    print ('thats crazy talk')

print (what_to_print)
