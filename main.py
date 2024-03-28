import requests
import json
import win32com.client as wincom

import time
# you can insert gaps in the narration by adding sleep calls

city = input("enter the name of the city: ")
url = f'http://api.weatherapi.com/v1/current.json?key=d8ecb906f5ea4e0794773156242202&q={city}'
r= requests.get(url)
print(r.text)
print(type(r.text))
wdic=json.loads(r.text)
w = wdic['current']['temp_c']
text = f"the current weather in {city} is  {w} degrees"
speak = wincom.Dispatch("SAPI.SpVoice")
speak.Speak(text)
# print(wdic["current"]["temp_c"])