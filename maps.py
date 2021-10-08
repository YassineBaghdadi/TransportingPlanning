# import gmplot
# from ipywidgets.embed import embed_minimal_html
# from datetime import datetime
# now = datetime.now()
# apikey = "AIzaSyDYpKJYTlRuA2aRAsfILNjxYJclDiTw9p4"
# start, end = (34.6846361,-1.9424976),(34.6846361,-1.9424976)
import json
import webbrowser

import firebase_admin
from firebase_admin import credentials, db

maps = [[34.7696791,-1.9393712], [34.6900348,-1.9197214], [34.6577664,-1.9171417]]
#
# gmap = gmplot.GoogleMapPlotter(35, -102, 5)
# gmap.apikey = apikey
# gmap.scatter([i[0] for i in waypoints], [i[1] for i in waypoints], 'red', size = 10)
# gmap.draw('mapstest.html')


# import required modules
# from selenium import webdriver
# from time import sleep
# 
# cred = credentials.Certificate("src/key.json")
# firebase_admin.initialize_app(cred, {
#         'databaseURL': 'https://saccomxd-stm-yassine-baghdadi-default-rtdb.firebaseio.com/',
#     })
# 
# 
# def openTrajet(data : list):
#     drvs = db.reference('drivers')
# 
#     trip = drvs.child("said").child("trips").child("2022-09-15 17:00:00").child("tracking")
#     print(list(dict(trip.get()).values()))
#     # [print(v) for i, v in dict(trip.get()).items()]
#     # tripID = trip.child("id").get()
#     # trck = trip.child("tracking").get()
#     # done = []
#     # result = {}
#     # if trck:
#     #     for key, value in trck.items():
#     #         if value not in result.values() and value != '0':
#     #             result[key] = value
#     #
#     #     print(f"{result}")
#     # url = "https://www.google.com/maps/dir"
#     # for i in data:
#     #     url += f"/{i[0]},{i[1]}"
#     #
#     # webbrowser.open(url)
# 
# 
# openTrajet(maps)

#
# import folium
#
# # Define the center of our map.
# lat, lon = 34.6798096,-1.9062235
#
# oujda = folium.Map(location=[lat, lon], zoom_start=13.5)
#
# for i in maps:
#     folium.Marker(
#         i, popup="<i>Mt. Hood Meadows</i>", tooltip="yassine"
#     ).add_to(oujda)
#
#
# folium.PolyLine(maps,
#                 color='red',
#                 weight=2,
#                 opacity=0.8).add_to(oujda)
#
#
# oujda.save("mappppppp.html")

#
# import requests
# import urllib.parse
#
# address = 'route sidi yahya oujda'
# url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'
#
# response = requests.get(url).json()
# print(response)
# print(f'{response[0]["lat"]},{response[0]["lon"]}')

from ipregistry import IpregistryClient

client = IpregistryClient("tryout")
ipInfo = json.loads(str(client.lookup()))['location']

print(f"{ipInfo['latitude']},{ipInfo['longitude']}")