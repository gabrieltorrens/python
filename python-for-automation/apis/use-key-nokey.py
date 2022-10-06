import requests

baseUrl = 'http://api.openweathermap.org/data/2.5/forecast'
parameters = {'APPID': '{key}','q': 'Detroit,US' , }

response = requests.get(baseUrl, params = parameters)

print(response.content)