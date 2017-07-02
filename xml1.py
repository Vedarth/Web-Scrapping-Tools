import urllib.request,urllib.parse,urllib.error
import xml.etree.ElementTree as ET
import re
url = input('Enter URL-')
x = urllib.request.urlopen(url).read()
data = ET.fromstring(x)
x=list()
for dat in data.findall('.//count'):
    x.append(int(dat.text))
print(sum(x))
