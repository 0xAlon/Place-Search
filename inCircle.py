# -*- coding: utf-8 -*-

"""
    Testing if a point is inside a circle
        Using Pythagoras to measure the distance between location points and the centre points
        and see if it's lower than the radius

        √ (location_latitude - center_latitude)^2 + (location_longitude - center_longitude)^2 <= Radius
"""
import math

def inCircle():

    location_latitude # location latitude point
    location_longitude #location longitude point

    center_latitude #center latitude point
    center_longitude #center longitude point

    Radius = 200

    distance = math.sqrt((center_latitude - location_latitude) ** 2 + (center_longitude - location_longitude) ** 2)
    return distance <= Radius
