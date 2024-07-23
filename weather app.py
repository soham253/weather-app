import requests
import json

city=input("enter name of city")
url="https://api.weatherapi.com/v1/current.json?key=78507b421998413f90e72731231606&q={city}"
r=requests.get(url)

wdic=json.loads(r.text)
print(wdic["current"]["temp_c"])



s=input("enter command")


print(s)
text.say(s)
text.runAndWait()
