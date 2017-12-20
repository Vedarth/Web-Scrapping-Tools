import requests
bibtex_id = 'microsoft/'

url = "http://query.nytimes.com/search/sitesearch/#/{id}".format(id=bibtex_id)
xhr_url = 'http://query.nytimes.com/query.nytimes'

with requests.Session() as session:
    session.get(url)

    response = session.get(xhr_url, params={'id': bibtex_id})
    print(response.content)

