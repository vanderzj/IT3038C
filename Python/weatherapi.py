import json
import requests

r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Cincinnati&appid=9c183f64bda3e96b9d511256eaad8c3d')

data = r.json()

print(data)