import requests

while True:
    response = requests.get('http://api.cosmosbot.ga:9090/api')
    print(response.json())
