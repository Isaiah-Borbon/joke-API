import requests
import json
from pprint import pprint

url = "https://www.icanhazdadjoke.com"

payload={}
headers={'Accept': "application/json"}

response = requests.request ("GET", url, headers=headers, data=payload)

responseJson = response.json()

print("Sleepless nights are no fun, have a joke!" + str(responseJson['joke']))

