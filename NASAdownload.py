import requests
import os

def fetch_nasa_image():
    API = "fRXAVkBAbmlkd3GgxvIawG4jZM0VKlz9cUhz8U4Y"
    URL = "https://api.nasa.gov/planetary/apod"
    params = {"api_key": API}

    response = requests.get(URL, params=params)
    data = response.json()
    

    if "hdurl" in data:
        image_url = data["hdurl"]
    else:
        image_url = data["url"]

    image_data = requests.get(image_url).content
    #sends GET req to iamge URL, stores actual image (raw binary data) in image_data
    #requests.get(____).content is used for images, audio files, PDFs, videos, etc. 
    #  without .content, text/metadata is given
    #core part of REST API involving media/files

    file_name = f"{data['date']}_{data['title'].replace(" ", "_")}.jpg"

    with open(file_name, "wb") as f:#write-binary mode (OOP in python course), saves raw image data
                                    #'with' automatically closes file after writing
                                    #prevents bugs (file corruption, memory leaks), clean efficient file saving
                                    #used w many APIs to save images, audios, videos, logs, etc
                                    #very reusable
        f.write(image_data) 
        #writes binary image onto file on disk
        #applies any data: APIs returning PDFs, audios, images, videos, etc
        #basic but very good when used with 'requests' and file I/O

    print(f"Imaged successfully saved as {file_name}")