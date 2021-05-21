import requests
from tkinter import *
import math

api_key = "eab1ac4810f1c33ae966e33accfb994c"

def get_wether(api_key,city):
    url = f"http://api.openweathermap.org/data/2.5/forecast/daily?q={city}&appid={api_key}"
    response = requests.get(url).json()
    print(response)


get_wether(api_key,"Seattle,US")