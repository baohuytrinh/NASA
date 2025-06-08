import requests
import os
import ctypes #this is windows only, and is for setting wallpaper(s)
from datetime import datetime #as dt

API = 'fRXAVkBAbmlkd3GgxvIawG4jZM0VKlz9cUhz8U4Y'
URL = 'https://api.nasa.gov/planetary/apod'

def fetch_image_data(date=None):
    params = {'api_key': API}
    if date:
        params['date'] = date
    response = requests.get(URL, params=params)
    response.raise_for_status
    return response.json()

def download_image(image_url, filename):
    image_data = requests.get(image_url).content
    with open(filename, 'wb') as f:
        f.write(image_data)

def set_wallpaper(image_path): #windows only
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 0)
    #native way to chagen wallpaper in Windows, ctypes allows interaction w 
    #Windows-level features from python

def main():
    data = fetch_image_data()

    if data['hdurl'] in data:
        image_url = data['hdurl']
    else:
        image_url = data['url']

    filename = f"{data['date']}_{data['title'].replace(' ', '_')}.jpg"

    download_image(image_url, filename)


    if os.name == "nt": #nt = windows, posix = macOS/Linux
        set_wallpaper(os.path.abspath(filename))