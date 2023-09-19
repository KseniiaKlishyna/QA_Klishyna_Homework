import Homework_21.infrastructure as infra


def test_get_object():
    print(infra.get_an_object(4).json())
    assert infra.get_an_object(4).status_code == 200


def test_get_object_invalid_id():
    invalid_id = 100
    response = infra.get_an_object(invalid_id)
    assert response.status_code == 404


def test_get_object_missing_id():
    response = infra.get_an_object(" ")
    assert response.status_code == 404


def test_get_all_objects():
    response = infra.get_an_object("")
    assert response.status_code == 200


def test_get_object_large_id():
    large_id = 12345678901234567890
    response = infra.get_an_object(large_id)
    assert response.status_code == 404


def test_create_an_object():
    response, obj_id = infra.create_the_correct_object()
    get_response = infra.get_an_object(obj_id)
    assert response.status_code == 200
    assert get_response.status_code == 200
    print(get_response.json())


def test_create_object_empty_name():
    payload = {
        "data": {"color": "blue", "generation": "13 Pro Max", "price": 1600}
    }
    response = infra.create_an_object(payload)
    assert response.status_code == 200


def test_create_object_empty_data():
    payload = {
        "name": "Apple IPhone",
        "data": {}
    }
    response = infra.create_an_object(payload)
    assert response.status_code == 200


def test_create_object_large_payload():
    payload = {
        "name": "Apple IPhone",
        "data": {"color": "blue" * 10000}
    }
    response = infra.create_an_object(payload)
    assert response.status_code == 500

def test_update_object():
    response, obj_id = infra.create_the_correct_object()
    changed_obj = infra.update_an_object(obj_id, {"name": "name is no more Apple",
                                                  "data": {"color": "white", "generation": "3rd", "price": 135}})
    assert response.status_code == 200
    assert changed_obj.status_code == 200
    print(changed_obj.json())


def test_delete_object():
    response, obj_id = infra.create_the_correct_object()
    deleted_obj = infra.delete_an_object(obj_id)
    assert deleted_obj.status_code == 200
    print(deleted_obj.json())