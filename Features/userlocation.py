from geopy.geocoders import Nominatim
import requests

def get_user_location():
    try:
        response = requests.get('https://ipinfo.io')
        geoLoc = Nominatim(user_agent="GetLoc")
        data = response.json()
        coordinates=data['loc'].split(',')
        latitude=coordinates[0]
        longitude=coordinates[1]
        locname = geoLoc.reverse(data['loc'])
        response="Your are currently in "+locname.address+". Your latitude is "+latitude+" and your longitude is "+longitude
        return response
        
    except Exception as e:
        return "Unable to detect your location."
    