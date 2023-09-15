from requests import get

url = 'https://reqres.in/'
headers = {
    "ContentType": "application/json"
}
response_users = get(url + "api/users/?page=2", headers=headers)
response_planets = get(url + "api/planets/?page=2", headers=headers)
print(response_users.json())
print(response_planets.json())




