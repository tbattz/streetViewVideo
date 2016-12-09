'''
Created on 8Dec.,2016

@author: bcub3d-laptop
'''

import numpy as np
import urllib
import cv2
import googlemaps, polyline

def getImageFromUrl(url):
    '''Gets an image from irl and returns
    it as an opencv object.'''
    resp = urllib.urlopen(url)
    size = (int(resp.info().getheaders("Content-Length")[0])/1024.0)
    image = np.asarray(bytearray(resp.read()),dtype='uint8')
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    
    return image, size

def loadAPIKey(file):
    '''Loads the API Key string from a given file.'''
    f = open(file,'r')
    apiKey = f.readline()
    f.close()
    
    return apiKey

def getCoordsFromDirections(apiKey,origin,finish):
    '''Returns vectors of lat and lon for a path
    from the origin to finish. origin and finish
    are specified by strings, e.g. 'Melbourne, Victoria'.'''
    gmaps = googlemaps.Client(key=apiKey)
    directions_result = gmaps.directions(origin,finish)
    lineData = polyline.decode(directions_result[0]['overview_polyline']['points'])
    
    lats = []
    lons = []
    for pair in lineData:
        lats.append(pair[0])
        lons.append(pair[1])
    
    return lats, lons