from fastapi import FastAPI
import requests

api_key = "e18af146-48f4-4812-8387-f3f41ec0990b"
base_url = "https://api.airvisual.com/v2/"

app = FastAPI()

@app.get("/")
def home():
    return {"message": "hello world"}



@app.get("/city_data")
def get_nearest_city_data():
    test_url = f"{base_url}nearest_city?key={api_key}"
    response = requests.get(test_url)
    return response.json()



@app.get("/supported_countries")
def get_all_supported_countries():
    test_url = f"{base_url}countries?key={api_key}"
    response = requests.get(test_url)
    return response.json()



@app.get("/countries/{country}/supported_states")
def get_all_supported_states(country: str):
    test_url = f"{base_url}states?country={country}&key={api_key}"
    response = requests.get(test_url)
    return response.json()



@app.get("/countries/{country}/states/{state}/supported_cities")
def get_all_supported_cities(country: str, state: str):
    test_url = f"{base_url}cities?state={state}&country={country}&key={api_key}"
    response = requests.get(test_url)
    return response.json()



@app.get("/countries/{country}/states/{state}/cities/{city}")
def get_city_data(country: str, state: str, city: str):
    test_url = f"{base_url}city?city={city}&state={state}&country={country}&key={api_key}"
    response = requests.get(test_url)
    return response.json()



@app.get("/countries/{country}/states/{state}/cities/{city}/supported_stations")
def get_list_of_supported_stations_in_a_city(country: str, state: str, city: str):
    test_url = f"{base_url}stations?city={city}&state={state}&country={country}&key={api_key}"
    response = requests.get(test_url)
    return response.json()



@app.get("/nearest_station")
def get_nearest_station():
    test_url = f"{base_url}nearest_station?key={api_key}"
    response = requests.get(test_url)
    return response.json()



@app.get("/nearest_station/gps")
def get_station_data_by_gps(latitude: float, longitude: float):
    test_url = f"{base_url}nearest_station?lat={latitude}&lon={longitude}&key={api_key}"
    response = requests.get(test_url)
    return response.json()



@app.get("/station/data")
def get_city_data_by_gps(station_name: str, city: str, state: str, country: str):
    test_url = f"{base_url}station?station={station_name}&city={city}&state={state}&country={country}&key={api_key}"
    response = requests.get(test_url)
    return response.json()



@app.get("/countries/{country}/city_ranking")
def get_city_ranking(country: str):
    test_url = f"{base_url}city_ranking?country={country}&key={api_key}"
    response = requests.get(test_url)
    return response.json()
