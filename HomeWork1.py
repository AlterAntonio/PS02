import requests, pprint

response = requests.get('https://api.github.com/search/repositories', params={'q': 'html'})
print(response.status_code)
pprint.pprint(response.json())