import json
from math import radians, sin, cos, sqrt, asin
class Street:
    def __init__(self, lat, lon, name, number = '-'):
        self.name = name
        self.number = number
        self.lat = lat
        self.lon = lon
        self.distance = None
    
    def computeDistance(self, lat, lon):
        # Haversine distance
        R = 6372.8e3
        dLat, dLon = radians(lat - self.lat), radians(lon - self.lon)
        lat, _lat = radians(lat), radians(self.lat)

        a = sin(dLat / 2) ** 2 + cos(lat) * cos(_lat) * sin(dLon / 2) ** 2
        c = 2 * asin(sqrt(a))
        
        self.distance = R * c
        return self
    
    def __repr__(self):
        return f'<Street {self.name} number: {self.number} distance: {round(self.distance, 2)}m>'

class Stockholm:
    def __init__(self, fileName):
        self.f = open(fileName, mode='r', encoding='utf-8')
        self.streets = []
    def __enter__(self):
        _json = json.load(self.f)
        for s in _json:
            if len(s) == 3: 
                lat, lon, street = s.values()
                self.streets.append(Street(lat, lon, street))
            else: 
                lat, lon, number, street = s.values()
                self.streets.append(Street(lat, lon, street, number))

        return self
    
    def getStreets(self):
        return self.streets

    def __exit__(self, exc_type, exc_val, traceback):
        try:
            self.f.close()
        except AttributeError:
            return True