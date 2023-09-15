import pytest
from Homework_20.infrastructure.people_service import PeopleService
from Homework_20.infrastructure.planets_service import PlanetsService


@pytest.fixture()
def people_service():
    yield PeopleService()


@pytest.fixture()
def planets_service():
    yield PlanetsService()
