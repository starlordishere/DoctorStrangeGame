import urllib.request
import json
import random


url = f'https://api.adviceslip.com/advice'

def item():
  response = urllib.request.urlopen(url)
  result = json.loads(response.read())
  print(result['slip']['advice'])



