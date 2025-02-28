from models.user import User

class UserRepository:
    def __init__(self):
        self.users = {}
        self.next_id = 1

    def add_user(self, user):
        user_id = self.next_id
        self.users[user_id] = user
        self.next_id += 1
        return user_id

    def get_user(self, user_id):
        return self.users.get(user_id)

    def get_all_users(self):
        return self.users.values()

    def update_user(self, user_id, user):
        if user_id in self.users:
            self.users[user_id] = user
            return True
        return False

    def delete_user(self, user_id):
        return self.users.pop(user_id, None) is not None
