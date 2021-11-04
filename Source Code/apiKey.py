import requests
baseUrl = 'http://api.openweathermap.org/data/2.5/forecast'
parameters = {'APPID': '0bb7ba6fe4d891cde6a00eb51ecbe161','q':'Seattle, US'}
response = requests.get(baseUrl, params = parameters)
print(response.content)