from Homework_22.repositories.users_adapter import UsersAdapter
from Homework_22.session_handler import session


users_adapter = UsersAdapter(session)

def test_post_get():
    existing_user = users_adapter.sql_to_api_get('111')
    if existing_user:
        users_adapter.delete_user_by_sql('111')
    # Test POST
    new_user = users_adapter.api_to_sql_post('111', 'John', 'Doe', 30, 'john.doe@example.com')
    assert new_user is not None

    # Test GET
    retrieved_user = users_adapter.sql_to_api_get('111')
    assert retrieved_user is not None
    assert retrieved_user.first_name == 'John'


def test_insert_select():
    # Test INSERT
    users_adapter.insert_user_by_sql('111', 'John', 'Doe', 30, 'john.doe@example.com')

    # Test SELECT
    retrieved_user = users_adapter.sql_to_api_select()
    assert len(retrieved_user) > 0
    assert retrieved_user[0].first_name == 'John'


def test_put_update():
    existing_user = users_adapter.sql_to_api_get('111')
    if existing_user:
        users_adapter.delete_user_by_sql('111')

    # Test POST via API
    new_user = users_adapter.api_to_sql_post('111', 'John', 'Doe', 30, 'john@example.com')
    assert new_user is not None

    # Test PUT via API
    updated_user = users_adapter.api_to_sql_put('111', 'John Updated', 'Doe Updated', 35, 'john.updated@example.com')
    assert updated_user is not None

    # Test GET via SQL
    retrieved_user = users_adapter.sql_to_api_get('111')
    assert retrieved_user is not None
    assert retrieved_user.first_name == 'John Updated'
    assert retrieved_user.last_name == 'Doe Updated'
    assert retrieved_user.age == 35
    assert retrieved_user.email == 'john.updated@example.com'

    # Test SELECT via SQL
    retrieved_user_sql = users_adapter.sql_to_api_select()
    assert len(retrieved_user_sql) > 0
    assert retrieved_user_sql[0].first_name == 'John Updated'
    assert retrieved_user_sql[0].last_name == 'Doe Updated'
    assert retrieved_user_sql[0].age == 35
    assert retrieved_user_sql[0].email == 'john.updated@example.com'


def test_update_sql_then_put_and_check_via_api():
    existing_user = users_adapter.sql_to_api_get('112')
    if existing_user:
        users_adapter.delete_user_by_sql('112')

    # Update user details via SQL
    users_adapter.insert_user_by_sql('112', 'John SQL Updated', 'Doe SQL Updated', 40, 'john.sql@example.com')

    # Check the update via SQL SELECT
    updated_user_sql = users_adapter.sql_to_api_get('112')
    assert updated_user_sql is not None
    assert updated_user_sql.first_name == 'John SQL Updated'
    assert updated_user_sql.last_name == 'Doe SQL Updated'
    assert updated_user_sql.age == 40
    assert updated_user_sql.email == 'john.sql@example.com'

    # Update the same user via API PUT
    updated_user_api = users_adapter.api_to_sql_put('112', 'John API Updated', 'Doe API Updated', 45, 'john.api@example.com')
    assert updated_user_api is not None

    # Check the update via API GET
    retrieved_user_api = users_adapter.sql_to_api_get('112')
    assert retrieved_user_api is not None
    assert retrieved_user_api.first_name == 'John API Updated'
    assert retrieved_user_api.last_name == 'Doe API Updated'
    assert retrieved_user_api.age == 45
    assert retrieved_user_api.email == 'john.api@example.com'



if __name__ == "__main__":
    test_post_get()
    test_insert_select()
    users_adapter.truncate_table()
    test_put_update()
    session.close()


