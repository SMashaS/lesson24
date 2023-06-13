from threading import Thread
from time import sleep


def us_cities(country):
    cities = ['New York', 'Tampa', 'Chicago', 'Dallas', 'Miami', 'Seattle']
    for city in cities:
        print(f'The best city in {country} is {city}')
        sleep(1)


def world_countries():
    countries = ['Ukraine', 'the US of America', 'SAR', 'Brasil', 'Australia', 'China']
    for country in countries:
        print(f'The best country on the continent is {country}')
        sleep(0.5)


cities_thread = Thread(target=us_cities, daemon=True, kwargs={"country": "the United States of America"})
cities_thread.start()

countries_thread = Thread(target=world_countries)
countries_thread.start()
