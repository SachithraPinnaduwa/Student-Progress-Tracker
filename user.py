class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __str__(self):
        return f"User ID: {self.user_id}"
