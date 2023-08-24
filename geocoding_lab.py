from geopy.geocoders import Nominatim
from geopy.distance import geodesic

geolocator = Nominatim(user_agent ='Distance calculator')

cityA = (input("input a city: ")).capitalize()
cityB = (input("input another city: ")).capitalize()



try :
    
    locationA = geolocator.geocode(cityA)
    locationB = geolocator.geocode(cityB)

    A = (locationA.latitude, locationA.longitude)
    B = (locationB.latitude, locationB.longitude)

    Distance = geodesic(A, B)
    



    print(Distance)
    print(f'The distance between {cityA} and {cityB} is {Distance} ')
    
except:
    print("invalid input")
    


    


    
    


