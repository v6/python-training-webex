'''
This is week 5 of the training. 

This goes over how to use a basic API.
'''

import requests

print("This uses the yoda API")

response = requests.get("https://yoda.p.mashape.com/yoda?sentence=You+will+learn+how+to+speak+like+me+someday.",
  headers={
    "X-Mashape-Key": "kqa1v2hdUFmshdbT8dqo57dDMJE0p1LDY1HjsnlCuj56q4um3N",
    "Accept": "text/plain"
  }
)

print ( response.text )
