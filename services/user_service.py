from data.user_repository import UserRepository
from models.user import User, UserResponse
from datetime import datetime

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def create_user(self, first_name, last_name, birth_year, group):
        user = User(first_name, last_name, birth_year, group)
        user_id = self.user_repository.add_user(user)
        return user_id

    def get_user(self, user_id):
        user = self.user_repository.get_user(user_id)
        if user:
            age = datetime.now().year - user.birth_year
            return UserResponse(user_id, user.first_name, user.last_name, age, user.group)
        return None

    def get_all_users(self):
        users = self.user_repository.get_all_users()
        return [UserResponse(user_id, user.first_name, user.last_name, datetime.now().year - user.birth_year, user.group) for user_id, user in users.items()]

    def update_user(self, user_id, first_name, last_name, birth_year, group):
        user = User(first_name, last_name, birth_year, group)
        return self.user_repository.update_user(user_id, user)

    def delete_user(self, user_id):
        return self.user_repository.delete_user(user_id)
