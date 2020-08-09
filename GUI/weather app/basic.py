#*In this tutorial, i am going to build a weather app pulling from an API on airnow.org.
#*I will connect to an online API

#!When pulling data from an online API, always use JSON

from tkinter import *
from PIL import Image, ImageTk
import requests
import json

#http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=07670&distance=5&API_KEY=7FB77423-8F33-4BEB-A07D-ADD631EAA25D

root = Tk()
root.title("Weather app")
root.geometry("400x50")


try:
    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=07670&distance=5&API_KEY=7FB77423-8F33-4BEB-A07D-ADD631EAA25D")
    api = json.loads(api_request.content)
except Exception as e:
    api = "error"

my_label = Label(root, text=api)
my_label.pack()

mainloop()