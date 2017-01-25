'''Open Ten Tabs

This opens 10 tabs in your local browser. 

It uses the [webbrowser library](https://docs.python.org/3/library/webbrowser.html). 

Do not run it in your Vagrant, since you want to see it in your local browser.'''

import webbrowser  # https://docs.python.org/3/library/webbrowser.html

print("Opening 10 tabs using the webbrowser library")

for i in range(1, 10): 
    print ("test")
