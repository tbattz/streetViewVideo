## Requirements
# Google API Keys
The following Google APIs are required. Add them using https://developers.google.com/console.
- Google Maps Directions API
- Google Maps Distance Matrix API
- Google Maps Elevation API
- Google Maps Geocoding API
- Google Maps Roads API
- Google Maps Time Zone API
- Google Street View Image APi

Your overall key should be placed in the apiKey.txt file in the top direction. Note, this file is added to the .gitignore so that you will not accidentally commit your API key.

# Python Modules
You will also need the following modules
- googlemaps
- polyline
- LatLon

They can be installed using
```
sudo -H pip install googlemaps
sudo -H pip install polyline
sudo -H pip install LatLon
```