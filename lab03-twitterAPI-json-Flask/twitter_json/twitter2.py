import urllib.request, urllib.error
from scripts import twurl
import json
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print('')
# acct = input('Enter Twitter Account:')
acct = 'nasa'
# if (len(acct) < 1): break
url = twurl.augment(TWITTER_URL,
                    {'screen_name': acct, 'count': '100'})
print('Retrieving', url)
connection = urllib.request.urlopen(url, context=ctx)
data = connection.read().decode()

js = json.loads(data)

headers = dict(connection.getheaders())
print('Remaining', headers['x-rate-limit-remaining'])

print(len(js["users"]))
file = open('nasa1.json', 'w', encoding='utf-8')
print(json.dumps(js, ensure_ascii=False), file=file)
file.close()
