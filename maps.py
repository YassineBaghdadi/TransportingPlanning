# import gmplot
# from ipywidgets.embed import embed_minimal_html
# from datetime import datetime
# now = datetime.now()
# apikey = "AIzaSyDYpKJYTlRuA2aRAsfILNjxYJclDiTw9p4"
# start, end = (34.6846361,-1.9424976),(34.6846361,-1.9424976)
import webbrowser

maps = [[34.7696791,-1.9393712], [34.6900348,-1.9197214], [34.6577664,-1.9171417]]
#
# gmap = gmplot.GoogleMapPlotter(35, -102, 5)
# gmap.apikey = apikey
# gmap.scatter([i[0] for i in waypoints], [i[1] for i in waypoints], 'red', size = 10)
# gmap.draw('mapstest.html')


# import required modules
from selenium import webdriver
from time import sleep

def openTrajet(data : list):
    url = "https://www.google.com/maps/dir"
    for i in data:
        url += f"/{i[0]},{i[1]}"

    webbrowser.open(url)


openTrajet(maps)
