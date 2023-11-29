class User:
    def __init__(self, username, email, password, role):
        self.email = email
        self.username = username
        self.password = password
        self.role = role

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

    def set_username(self, new_username):
        self.username = new_username

    def set_email(self, new_email):
        self.email = new_email

    def set_password(self, new_password):
        self.password = new_password

    def set_role(self, new_role):
        self.role = new_role
