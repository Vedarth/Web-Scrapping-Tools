import json
import urllib.request,urllib.parse,urllib.error
url='http://py4e-data.dr-chuck.net/comments_3052.json'
print('Retrieving',url)
uh = urllib.request.urlopen(url)
data = uh.read()

info = json.loads(data.decode())
print('Retrieved', len(json.dumps(data.decode())),'characters')
count = 0
for item in info['comments']:
    count = count + item['count']
print(count)
