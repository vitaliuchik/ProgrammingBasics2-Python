from flask import Flask, render_template, request


import urllib.request, urllib.parse, urllib.error
from scripts import twurl
import json
import ssl
import folium

from geopy.geocoders import MapBox
from geopy.exc import GeocoderServiceError

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

geolocator = MapBox(api_key='pk.eyJ1Ijoicm9tYW4yMjIzNCIsImEiOiJjanJ1b2lkdmgxNWhoNDNxc3B4Y2o0dnE4In0.-o_eVMh-dV2YuhI8qbtp-Q')



def get_json(acct):
    if len(acct) > 1:
        url = twurl.augment(TWITTER_URL,
                            {'screen_name': acct, 'count': '100'})
        connection = urllib.request.urlopen(url, context=ctx)
        data = connection.read().decode()
        js = json.loads(data)
        loc = dict()
        for u in js['users'] :
            loc[u['location']] = loc.get(u['location'], list())
            loc[u['location']].append(u['screen_name'])
        return loc


def geo(loc):
    locations = []
    for key in loc:
        try:
            location = geolocator.geocode(key)
            locations.append([loc[key], [location.latitude, location.longitude]])
        except (AttributeError, NameError, GeocoderServiceError):
            pass
    return locations


def build_map(locations):
    map = folium.Map()
    for loc in locations:
        folium.Marker(loc[1], popup=', '.join(loc[0])).add_to(map)
    map.save('templates/map.html')


build_map(geo(get_json('nasa')))


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def register():
    username = request.form["register"]
    build_map(geo(get_json(username)))
    return render_template("map.html")


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)