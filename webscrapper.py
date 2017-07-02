import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl
cert = ssl.create_default_context()
cert.check_hostname = False
cert.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=cert).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('img')
for i in range(len(tags)):
    
    try:
        x = tags[i].get('src',None).strip().split('/')[-1].strip()
        urllib.request.urlretrieve(tags[i].get('src',None),x+'.jpg')
    except:
        continue
