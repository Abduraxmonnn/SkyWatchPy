# Python
import requests


# Project
from configs.KEYS import API_KEY, API_URL


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
