from math import radians, sin, cos, sqrt, atan2


class User:
    def __init__(self, location=(46.771290, 23.596131)):
        self.location = location
    

    def update_score(self, apt_loc):
        lat, long = self.location

        a_lat, a_long = apt_loc


        self.location = (
            (lat + a_lat) / 2,
            (long + a_long) / 2
        )

def haversine(location, user_coords=(46.771290, 23.596131)):
    R = 6371  # Radius of the Earth in kilometers

    lat1, lon1 = user_coords
    lat2, lon2 = location

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c




