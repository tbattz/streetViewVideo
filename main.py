'''
Created on 8Dec.,2016

@author: bcub3d-laptop
'''

import tools as tl
import cv2
import LatLon
import matplotlib.pyplot as plt

# Load APi Key
apiKey = tl.loadAPIKey('apiKey.txt')

# Get points
origin = 'Melbourne VIC 3004'
finish = 'Melbourne Cricket Ground, Brunton Avenue, Richmond VIC 3002'
lats, lons = tl.getCoordsFromDirections(apiKey, origin, finish)

# Calculates Heading
heading = []
for i in range(0,len(lats)-1):
    start = LatLon.LatLon(LatLon.Latitude(lats[i]),LatLon.Longitude(lons[i]))
    finish = LatLon.LatLon(LatLon.Latitude(lats[i+1]),LatLon.Longitude(lons[i+1]))
    heading.append(start.heading_initial(finish))
heading.append(heading[-1])

#plt.plot(lons,lats,'*')
#plt.show()

# Create Video writer
fourcc = cv2.cv.CV_FOURCC('X','V','I','D')
out = cv2.VideoWriter('output2.avi',fourcc,5.0,(640,640),True)

# Get Image
for i in range(0,len(lats)):
    size = '640x640' # Largest size avaliable for free use
    location = '%.6f,%.6f' % (lats[i],lons[i])
    pitch = '-0.76'
    
    url = 'https://maps.googleapis.com/maps/api/streetview?size=%s&location=%s&heading=%s&pitch=%s&key=%s' % (size,location,str(heading[i]),pitch,apiKey)
    
    image, size = tl.getImageFromUrl(url)
    #cv2.imshow("Image",image)   
    #cv2.waitKey(0)

    # Write video
    out.write(image)
    print '%i/%i' % (i+1,len(lats))
    
# Finish Video
out.release()
cv2.destroyAllWindows()


