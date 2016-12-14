'''
    Tell jokes and visit websites

    This opens several websites & tells some jokes using the 
    webbrowser library. 
'''
import webbrowser
from webbrowser import open, open_new
print ('This is a joke, folks.')


print ('hello guys, vagrant is not working on windows')

print ('yo this auto updates')

my_list = ['appl', 'android', 'windows']

for platform in my_list:
    print(platform)
    webbrowser.open_new('https://duckduckgo.com/' + platform)
