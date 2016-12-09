'''
Created on 8Dec.,2016

@author: bcub3d-laptop
'''

import tools as tl
import cv2
import matplotlib.pyplot as plt

# Load APi Key
apiKey = tl.loadAPIKey('apiKey.txt')

# Get points
origin = 'Melbourne, Australia'
finish = 'Sydenham, Victoria'
lats, lons = tl.getCoordsFromDirections(apiKey, origin, finish)

# Get Image
for i in range(0,10):
    size = '640x640' # Largest size avaliable for free use
    location = '%.6f,%.6f' % (lats[i],lons[i])
    heading = '150.0'
    pitch = '-0.76'
    
    url = 'https://maps.googleapis.com/maps/api/streetview?size=%s&location=%s&heading=%s&pitch=%s&key=%s' % (size,location,heading,pitch,apiKey)
    
    image, size = tl.getImageFromUrl(url)
    cv2.imshow("Image",image)   
    cv2.waitKey(0)



