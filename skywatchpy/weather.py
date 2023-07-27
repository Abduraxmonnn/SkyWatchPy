# Python
import requests


# Project
from skywatchpy.KEYS import API_KEY, API_URL
from skywatchpy.countries import countries_name


def change_type_number(number_from_to=None):
    return float if number_from_to is None else number_from_to


class Current(object):
    url_result = API_URL + API_KEY

    def __init__(self, city_name='Tashkent'):
        self.city_name = city_name

    def set_city_name(self, city_name):
        self.city_name = city_name

    def __request_to_server(self):
        return requests.get(self.url_result.format(self.city_name)).json()

    def all_data(self):
        return self.__request_to_server()

    def weather_data(self):
        return self.__request_to_server()['weather']

    def get_city_name(self):
        return self.city_name

    def get_country_name(self):
        return countries_name[f"{self.__request_to_server()['sys']['country']}"]

    def coordinates(self):
        return self.__request_to_server()['coord']

    def get_lon(self, format_data=None):
        format_data = change_type_number(format_data)
        return format_data(self.__request_to_server()['coord']['lon'])

    def get_lat(self, format_data=None):
        format_data = change_type_number(format_data)
        return format_data(self.__request_to_server()['coord']['lat'])

    def get_temperature(self):
        return self.__request_to_server()['main']['temp_min']

    def get_min_temperature(self, format_data=None):
        format_data = change_type_number(format_data)
        return format_data(self.__request_to_server()['main']['temp_min'])

    def get_max_temperature(self, format_data=None):
        format_data = change_type_number(format_data)
        return format_data(self.__request_to_server()['main']['temp_max'])

    def get_pressure(self, format_data=None):
        format_data = change_type_number(format_data)
        return format_data(self.__request_to_server()['main']['pressure'])

    def get_humidity(self, format_data=None):
        format_data = change_type_number(format_data)
        return format_data(self.__request_to_server()['main']['humidity'])

    def get_visibility(self, format_data=None):
        format_data = change_type_number(format_data)
        return format_data(self.__request_to_server()['visibility'])

    def wind(self):
        return self.__request_to_server()['wind']

    def get_wind_speed(self, format_data=None):
        format_data = change_type_number(format_data)
        return format_data(self.__request_to_server()['wind']['speed'])

    def get_wind_degree(self, format_data=None):
        format_data = change_type_number(format_data)
        return format_data(self.__request_to_server()['wind']['deg'])

    def get_sunrise(self):
        return self.__request_to_server()['sys']['sunrise']

    def get_sunset(self):
        return self.__request_to_server()['sys']['sunset']

    def get_timezone(self):
        return self.__request_to_server()['timezone']
