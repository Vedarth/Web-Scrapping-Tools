import urllib.request,urllib.parse,urllib.error
fhandle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in fhandle:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
x = (([(value,key) for key,value in counts.items()]))
x.sort(reverse=True)
print(x)
