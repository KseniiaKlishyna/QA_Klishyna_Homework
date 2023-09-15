from Homework_20.conftest import people_service,planets_service

def test_test_luke(people_service):
    response = people_service.get_people("1")
    assert response.json()['name'] == 'Luke Skywalker'


def test_new_planet(planets_service):
    response = planets_service.get_planets("2")
    assert response.json()['name'] == 'Alderaan'
