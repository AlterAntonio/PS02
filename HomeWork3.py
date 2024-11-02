import requests

url = 'https://api.github.com/search/repositories'
data = {'title': 'foo', 'body': 'bar', 'userId': 1}

response = requests.get(url, data=data)
print(response.status_code)
print(response.json())