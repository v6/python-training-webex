'''
Install Python 3.5 from https://www.python.org/downloads/.
Set up the Integrated Learning Development Environment. DONE
IF Using Mac, install brew.sh and cask caskroom.io
IF using Windows, install scoop.sh
IF on Mac, install git from git-scm.com. 
Install the github desktop client if you're on Windows from desktop.github.com.
Install virtualbox (https://www.virtualbox.org/)
Install vagrant (https://www.vagrantup.com/)
Install the CEntOS 7.2 Vagrant Box
    git clone https://github.com/v6/python-training-webex.git
    cd python-training-webex
    vagrant up

We'll want to make small projects we can show people we know to prove 
the benefit of this, even something as simple as automating 
two or three commands with import subprocess.

Later sessions could show how to use virtual environments, wrap local scripts with a REST interface, or how to use client.py for automating Jabber.

If there’s time, we could go over veXMPP, my White Whale, as well.

Show a quick and duuurrrrty way to run Python in current bash scripts.
  echo -e "import sys\nfor r in range(10): print ('rob')" | python3
  python - <<EOF
  import sys
  for r in range(3): print 'rob'
  EOF
Introduce the Python philosophy.
https://youtu.be/npjOSLCR2hE
Run 'import this’.
Run 'import antigravity’.
show the help(), for example, x = 9, help(x)
https://docs.python.org/3/tutorial/introduction.html
>>> 'Py' 'thon'
'Python'

>>> word[:2] + word[2:]
'Python'
>>> word[:4] + word[4:]
'Python'

Demonstrate flow control.
Demonstrate data structures.

    Demonstrate Dictionaries and assignment. # https://docs.python.org/3/tutorial/datastructures.html#dictionaries
    a = 10
    >>> b = 20
    >>> a = b
    >>> print (a , b)
    20 20
    >>> myDict = {'ab':20, 'ab2':10}
    >>> myDict
    {'ab2': 10, 'ab': 20}
    >>> myDict['ab']
    20
    >>>    
    Slicing?
    >>> x = [1,2,3,4,5]
    >>> x[2:]
    [3, 4, 5]
Demonstrate imports.
import subprocess # https://docs.python.org/3/library/subprocess.html
'''
