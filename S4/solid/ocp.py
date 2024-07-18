class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def get_user_info(self):
        return f"Username: {self.username}, Email: {self.email}"

    def save_to_database(self):
        print(f"Saving {self.username} to the database.")

    def send_email(self, message):
        print(f"Sending email to {self.email}: {message}")


# after --------------------------------------------------------------------------------------------------------------
class User2:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def get_user_info(self):
        return f"Username: {self.username}, Email: {self.email}"


class UserDatabase:
    @staticmethod
    def save(user):
        print(f"Saving {user.username} to the database.")


class EmailService:
    @staticmethod
    def send_email(user, message):
        print(f"Sending email to {user.email}: {message}")


user = User("john_doe", "john@example.com")
print(user.get_user_info())
UserDatabase.save(user)
EmailService.send_email(user, "Welcome to our service!")
