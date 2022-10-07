import urllib.request
import json
key= 'ab5bf4b0970860437fc442604639d812'



def weather():

  city = 'toronto' #random city used
  url =f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}' #url to read weather data
  response = urllib.request.urlopen(url) #fetching url
  result = json.loads(response.read())
  
  temp_c = result["main"]["temp"]- 273.15 #temp in Kelvin, so subtracted 273.15 to change to celcius
  print(f"{round(temp_c,2)}C")


