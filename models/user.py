class User:
    def __init__(self, first_name, last_name, birth_year, group):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.group = group

class UserResponse:
    def __init__(self, user_id, first_name, last_name, age, group):
        self.id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.group = group
