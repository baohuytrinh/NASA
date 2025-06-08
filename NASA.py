import requests #
#HTTP requests, like GET and POST from Python itself
#very common when working with APIs in Python

API = "fRXAVkBAbmlkd3GgxvIawG4jZM0VKlz9cUhz8U4Y" # #most API need key, can be passed as param/headers in other cases
URL = "https://api.nasa.gov/planetary/apod" # #stores the API endpoint URL, will need more for complex APIs like Spot/Twit

params = {"api_key": API} #
#dict of query parameters, GET request, can be customized with cities, dates, terms, etc

response = requests.get(URL, params=params) #



if response.status_code == 200: #
    data = response.json() # #always call after getting response (200) and not (401, 404, etc)
    print("Title:", data["title"])
   #print("Explanation:", data["explanation"])
    print("Date:", data["date"])
    print("Image URL:", data["url"])

    #can print(data) to see the contents and follow/read responses (title, explanation)
else:
    print("Error:", response.status_code, response.text) #debugs invalid key, rate limit exceeded, bad query input
    #for others, we can try retrying, logging, user-friendly messages instead/addition