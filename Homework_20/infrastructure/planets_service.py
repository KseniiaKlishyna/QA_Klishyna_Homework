from requests import get, Response
from Homework_20 import config


class PlanetsService:
    def __init__(self):
        self.__planets_url = f"{config['host']}/planets"

    def get_planets(self, planets_id: str) -> Response:
        return get(f"{self.__planets_url}/{planets_id}")
