import Homework_21_.infrastructure as infra


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
    get_response = infra.get_an_object(payload)
    assert response.status_code == 200
    assert response.json()['name'] == None
    print(get_response.json())
    assert response.status_code == 200



def test_create_object_empty_data():
    payload = {
        "name": "Apple IPhone",
        "data": {}
    }
    get_response = infra.get_an_object(payload)
    response = infra.create_an_object(payload)
    assert response.status_code == 200
    print(get_response.json())
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


def test_update_object_with_large_payload():
    response, obj_id = infra.create_the_correct_object()
    large_payload = {
        "name": "New Name",
        "data": {
            "color": "black",
            "additional_data": "x" * (10 * 1024 * 1024)
        }
    }
    changed_obj = infra.update_an_object(obj_id, large_payload)
    assert response.status_code == 200
    assert changed_obj.status_code == 413

def test_update_object_with_invalid_id():
    invalid_id = "invalid_id"
    changed_obj = infra.update_an_object(invalid_id, {"name": "New Name"})
    assert changed_obj.status_code == 404


def test_update_object_with_invalid_id():
    invalid_id = "invalid_id"
    invalid_payload = {"name": "New Name"}
    expected_error = {
        "error": f"The Object with id = {invalid_id} doesn't exist. Please provide an object id which exists or generate a new Object using POST request and capture the id of it to use it as part of PUT request after that."
    }
    changed_obj = infra.update_an_object(invalid_id, invalid_payload)
    assert changed_obj.status_code == 404
    assert changed_obj.json() == expected_error


def test_update_object_with_valid_payload():
    response, obj_id = infra.create_the_correct_object()
    changed_obj = infra.update_an_object(obj_id, {"name": "New Name", "data": {"color": "black"}})
    assert response.status_code == 200
    assert changed_obj.status_code == 200
    assert changed_obj.json()['name'] == "New Name"
    assert changed_obj.json()['data']['color'] == "black"
    print(changed_obj.json())


def test_delete_object():
    response, obj_id = infra.create_the_correct_object()
    deleted_obj = infra.delete_an_object(obj_id)
    assert deleted_obj.status_code == 200
    print(deleted_obj.json())


def test_delete_nonexistent_object():
    non_existent_id = "non_existent_id"
    deleted_obj = infra.delete_an_object(non_existent_id)
    assert deleted_obj.status_code == 404

def test_delete_object_twice():
    response, obj_id = infra.create_the_correct_object()
    deleted_obj1 = infra.delete_an_object(obj_id)
    assert deleted_obj1.status_code == 200
    deleted_obj2 = infra.delete_an_object(obj_id)
    assert deleted_obj2.status_code == 404


def test_delete_object_with_invalid_id():
    invalid_id = "invalid_id"
    deleted_obj = infra.delete_an_object(invalid_id)
    assert deleted_obj.status_code == 404


def test_delete_object_with_valid_id():
    response, obj_id = infra.create_the_correct_object()
    deleted_obj = infra.delete_an_object(obj_id)
    expected_message = {"message": f"Object with id = {obj_id} has been deleted."}
    assert deleted_obj.status_code == 200
    assert deleted_obj.json() == expected_message
    print(expected_message)
    print(deleted_obj.json)