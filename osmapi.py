#!/usr/bin/env python
import Domoticz
from geopy.geocoders import Nominatim

class osmapi:
    def __init__(self):
        return

    def getaddress(self,lat,lon):
        geolocator = Nominatim(user_agent="domoticz-geofence")
        location = geolocator.reverse((lat, lon), timeout=10, exactly_one=True, addressdetails=True)
        roads = ['road', 'footway', 'pedestrian', 'cycleway', 'bridleway']
        count = 0
        street = ""
        while count < len(roads) and not street:
            street = location.raw['address'].get(roads[count], '')
            count += 1
        housenr = location.raw['address'].get('house_number', '')
        villages = ['city', 'town', 'village', 'hamlet', 'suburb']
        count = 0
        city = ""
        while count < len(villages) and not city:
            city = location.raw['address'].get(villages[count], '')
            count += 1
        country = location.raw['address'].get('country_code', '')
        req = "{} {}, {}, {}".format(street, housenr, city, country)
        return req
