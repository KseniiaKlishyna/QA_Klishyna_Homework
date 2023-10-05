from Homework_22.models.users import Users
from sqlalchemy.orm import Session
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError

class UsersAdapter:
    def __init__(self, session: Session):
        self.session = session




    def api_to_sql_post(self, user_id, first_name, last_name, age, email):
        user = Users(id=user_id, first_name=first_name, last_name=last_name, age=age, email=email)
        self.session.add(user)
        self.session.commit()
        return user

    def api_to_sql_put(self, user_id, first_name, last_name, age, email):
        user = self.session.query(Users).filter_by(id=user_id).first()
        if user:
            user.first_name = first_name
            user.last_name = last_name
            user.age = age
            user.email = email
            self.session.commit()
            return user

    def sql_to_api_get(self, user_id):
        return self.session.query(Users).filter_by(id=user_id).first()

    def sql_to_api_select(self):
        return self.session.query(Users).all()

    def insert_user_by_sql(self, user_id, first_name, last_name, age, email):
        try:
            self.session.execute(
                text(
                    "INSERT INTO tablewithusers (id, first_name, last_name, age, email) "
                    "VALUES (:user_id, :first_name, :last_name, :age, :email)"
                ),
                {"user_id": user_id, "first_name": first_name, "last_name": last_name, "age": age, "email": email}
            )
            self.session.commit()
        except IntegrityError as e:
            self.session.rollback()

    def truncate_table(self):
        try:
            self.truncate_table()
        except Exception as e:
            self.session.rollback()
            raise e

    def delete_user_by_sql(self, user_id):
        user = self.session.query(Users).filter_by(id=user_id).first()
        if user:
            self.session.delete(user)
            self.session.commit()