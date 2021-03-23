# Imports necessary modules.
import json
import requests

# Gets data from local API (api.js)
r = requests.get('http://localhost:3000')
data = r.json()

# Loops through every member of the list "data" and prints the name and color with some formatting. 
i = 0
while i < len(data):
    i = i + 1
    print(data[i - 1]['name'] + ' is ' + data[i - 1]['color'])