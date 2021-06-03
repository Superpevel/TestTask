import requests
import json
url = 'http://jsonplaceholder.typicode.com/albums' 
response = requests.get(url)

data = jsonRes = response.json() 
for x in data :
    print(x['userId'] ,end=' ')
    print(x['id'] ,end = ' ')
    print(x['title'], end = '\n')