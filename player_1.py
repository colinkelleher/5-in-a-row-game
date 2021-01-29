class Client():
    def __init__(self, username=''):
        self.username = username

    def inputUsername(self):
        self.username = input("Please enter your username: ")

    