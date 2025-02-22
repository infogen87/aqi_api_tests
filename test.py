import requests

api_key = "e18af146-48f4-4812-8387-f3f41ec0990b" #your api key
country = "nigeria"
state = "rivers"
city = "Port Harcourt"
longitude = 6.5000
latitude = 3.3500
station_name = ""


# # to get general data from the api



# # GET List of supported countries

url = f"http://api.airvisual.com/v2/countries?key={api_key}"




# #GET List of supported states in a country
# # url = f"http://api.airvisual.com/v2/states?country={country}&key={api_key}"


# #GET List of supported cities in a state

# # url = f"http://api.airvisual.com/v2/cities?state={state}&country={country}&key={api_key}"



# #GET nearest city data (IP geolocation)
# # url = f"http://api.airvisual.com/v2/nearest_city?key={api_key}"



# #Get nearest city data (GPS coordinates)
# # url = f"http://api.airvisual.com/v2/nearest_city?lat={latitude}&lon={longitude}&key={api_key}"


# # GET specified city data
# # url = f"http://api.airvisual.com/v2/city?city={city}&state={state}&country={country}&key={api_key}"



# # # GET List of supported stations in a city
# # # url = f"http://api.airvisual.com/v2/stations?city={city}&state={state}&country={country}&key={api_key}"


# # # GET nearest station data (IP geolocation)
# url = f"http://api.airvisual.com/v2/nearest_station?key={api_key}"

# #Get nearest station data (GPS coodinates)
# url = f"http://api.airvisual.com/v2/nearest_station?lat={latitude}&lon={longitude}&key={api_key}"

# #Get specified station data
# url = f"http://api.airvisual.com/v2/station?station={station_name}&city={city}&state={state}&country={country}&key={api_key}"


# #Get global city ranking
# url = f"http://api.airvisual.com/v2/city_ranking?key={api_key}&sort=&country={country}"

# # 
def get_result(test_url):

    response = requests.get(test_url)
    data = response.json()
    print(data) 




get_result(url)    