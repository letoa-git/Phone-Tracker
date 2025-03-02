print ( """
|   _  \  |  |  |  |  /  __  \  |  \ |  | |   ____|   |           ||   _  \         /   \     /      ||  |/  / |   ____||   _  \     
|  |_)  | |  |__|  | |  |  |  | |   \|  | |  |__      `---|  |----`|  |_)  |       /  ^  \   |  ,----'|  '  /  |  |__   |  |_)  |    
|   ___/  |   __   | |  |  |  | |  . `  | |   __|         |  |     |      /       /  /_\  \  |  |     |    <   |   __|  |      /     
|  |      |  |  |  | |  `--'  | |  |\   | |  |____        |  |     |  |\  \----. /  _____  \ |  `----.|  .  \  |  |____ |  |\  \----.
| _|      |__|  |__|  \______/  |__| \__| |_______|       |__|     | _| `._____|/__/     \__\ \______||__|\__\ |_______|| _| `._____|
                        ,===:'.,            `-._                           
                             `:.`---.__         `-._                           
                               `:.     `--.         `.                     
                                 \.        `.         `.                   
                         (,,(,    \.         `.   ____,-`.,      by : letoa & MaciSlam          
                      (,'     `/   \.   ,--.___`.'                         
                  ,  ,'  ,--.  `,   \.;'         `                         
                   `{D, {    \  :    \;                                    
                     V,,'    /  /    //                                    
                     j;;    /  ,' ,-//.    ,---.      ,                    
                     \;'   /  ,' /  _  \  /  _  \   ,'/                    
                           \   `'  / \  `'  / \  `.' /                     
                            `.___,'   `.__,'   `.__,'                                                                                                                         
                                                                         
                                                    

⠀⠀⠀⠀⠀⠀⠀""")
import phonenumbers
from phonenumbers import geocoder
import folium
from opencage.geocoder import OpenCageGeocode


key = input("Enter your OpenCage API key: ")


number = input("Enter phone number with country code ): ")


check_number = phonenumbers.parse(number)
number_location = geocoder.description_for_number(check_number, 'en')
print(f"Location (based on phone number region): {number_location}")


from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(f"Service Provider: {carrier.name_for_number(service_provider, 'en')}")


geocoder = OpenCageGeocode(key)


query = f"{number_location}, Georgia, country"  # Force the query to recognize Georgia as a country
results = geocoder.geocode(query)

if results:
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    print(f"Latitude: {lat}, Longitude: {lng}")


    map_location = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker([lat, lng], popup=number_location).add_to(map_location)


    map_location.save('map.html')
else:
    print("No results found for the given location.")
