import turtle
import requests
from geopy.geocoders import Nominatim
import time

from background import Background

image = "images/iss.gif"
screen = turtle.Screen()
background = Background()
screen.register_shape(image)
# space_station.shape("images/iss.png")
space_station = turtle.Turtle(image)
space_station.shape(image)
space_station.penup()

BATTERSEA_LAT = 36.144909
BATTERSEA_LONG = 5.353250
geolocator = Nominatim(user_agent="geoapiExercises")

screen.setworldcoordinates(-180, -90, 180, 90)

is_it_over = True
space_station.hideturtle()
space_station.penup()
while is_it_over:
    api_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    api_data = api_response.json()
    iss_latitude = float(api_data["iss_position"]["latitude"])
    iss_longitude = float(api_data["iss_position"]["longitude"])
    space_station.goto(iss_longitude, iss_latitude)
    if iss_longitude > 179:
        space_station.penup()
    else:
        space_station.pendown()
    space_station.showturtle()
    time.sleep(1)

# if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
#     print(f"Yes\nIt is currently {location}.")
# else:
#     print(f"No\nIt is currently {location}.")
screen.mainloop()
