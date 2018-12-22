"""
        Module: Get JSON object from Google Places API and find the place with the highest rating.
        Created: Nov 11, 2107 05:39PM
"""

import json, time, requests

URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=,&radius=&type=&key="

r = requests.get(URL)

max = 0

for x in r.json()['results']:
    if x.get('rating') != None: # Check if key (rating) exists in the JSON object
        if x['rating'] > max: # Compare  the key (rating) to the maximum value
            max = x['rating']
            #print x['name'].encode("utf8")
            #print x['geometry']['location']
            #print x['rating']
            #print x['types']

if r.json().get('next_page_token') != None: # Check if key (next_page_token) exists in the JSON object
    while r.json().get('next_page_token') != None:
        #print tmp.get('next_page_token')
        time.sleep(2)
        URL1 = URL + '&pagetoken=' + r.json().get('next_page_token')
        r = requests.get(URL1)
        for x in r.json()['results']:
            if x.get('rating') != None: # Check if key (rating) exists in the JSON object
                if x['rating'] > max: # Compare  the key (rating) to the maximum value
                    max = x['rating']

                    #print x['name'].encode("utf8")
                    #print x['geometry']['location']
                    #print x['rating']
                    #print x['types']

        #print URL1
        #print r.json()

print max
"""
        name     -- A term to be matched against the names of Places. Results will
                    be restricted to those containing the passed name value.

        opennow  -- Returns only those Places that are open for business at the time
                    the query is sent

        lat_lng  -- A dict containing the following keys: lat, lng (default None)

        radius   -- The radius (in meters) around the location/lat_lng to restrict
                    the search to. The maximum is 50000 meters (default 3200)

        type     -- An optional type used for restricting the results to Places (default None)

        types    -- An optional list of types, restricting the results to Places (default [])
                    This kwarg has been deprecated in favour of the 'type' kwarg.

"""
