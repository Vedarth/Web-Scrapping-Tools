import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
def scrape(url,count):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,'html.parser')
    tags = soup('a')
    count = count - 1
    if count>=0:
        temp=0
        for tag in tags:
            x=tag.get('href',None)
            if x is None:
                continue
            else:
                temp = temp + 1
            if temp == 18:
                return(scrape(x,count))
        
    else:
        temp = 0
        for tag in tags:
            x=tag.get('href',None)
            if x is None:
                continue
            else:
                temp = temp + 1
                if temp == 18:
                    return(x)
        

url = input('Enter URL- ')
print (scrape(url,6).split('_')[2].split('.')[0])
