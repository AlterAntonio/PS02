import requests

url = 'https://jsonplaceholder.typicode.com/posts'
params = {'userId': '1'}

response = requests.get(url, params=params)
for i in response.json():
    print(i)