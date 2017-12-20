from nytimesarticle import articleAPI
import json
import requests
for i in range(11,21):
	for j in range(12):
		if i==19 and j==12:
			break
		r = requests.get('http://api.nytimes.com/svc/archive/v1/{yr}/{mos}.json?api-key=cff873c19d5449c5a75ec55405eb76e4'.format(yr=1997+i, mos=j+1))
		data = json.loads(r.text)
		print(r.text[:500])
		fh = open('{yr}-{mos}.txt'.format(yr=1997+i, mos=j+1), 'a+')
		news = [data['response']['docs'][k]['snippet'] for k in range(len(data['response']['docs']))]
		fh.write(str(news).decode('utf-8').encode('cp850','replace').decode('cp850'))
		fh.close()