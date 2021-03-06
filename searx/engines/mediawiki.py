from json import loads
from urllib import urlencode, quote

url = 'https://en.wikipedia.org/'

number_of_results = 10

def request(query, params):
    search_url = url + 'w/api.php?action=query&list=search&{query}&srprop=timestamp&format=json'
    params['url'] = search_url.format(query=urlencode({'srsearch': query}))
    return params


def response(resp):
    search_results = loads(resp.text)
    results = []
    res = search_results.get('query', {}).get('search', [])
    if not len(res):
        return results
    for result in res[:int(number_of_results)]:
        results.append({'url': url + 'wiki/' + quote(result['title'].replace(' ', '_').encode('utf-8')), 'title': result['title']})
    return results

