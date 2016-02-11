#!/usr/bin/env python3
 
# The above line is not necessary for Windows, because paths are configured globally...

'''
This module helps to test network connectivity.

Ping a list of ipaddresses, in order, to determine access. 
This module also will help test connectivity to Messenger servers. 
Credits: Messenger Service Engineering, specifically Reggie/Nathan

'''

import subprocess

my_command = subprocess.call(['ls', '-a'])

iplist = ['192.168.1.20', '10.0.0.1', '10.0.0.5']

def iptest():
    '''Test IP addresses from an previously defined list, and display results.'''
    for ip in iplist:
        print (ip)
        subprocess.call(['ping', '-c', '2', ip]) 

def crazy_talk(): #{ start of function
    sane_variable = 2
    what_to_print = ''
    crazy_variable = 10000000
    if crazy_variable == sane_variable:
        what_to_print = 'hello world'
    else:
        print ('thats crazy talk')
    if crazy_variable*crazy_variable == 25: 
        print ('this is NOT crazy talk')
    else: 
        print ('thats crazy talk')
    
    print (what_to_print)
    #} end of function
