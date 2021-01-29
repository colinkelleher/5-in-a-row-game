import socket
import sys

class Client():
    def __init__(self, username=''):
        self.username = username

    def inputUsername(self):
        self.username = input("Please enter your username: ")

    def connectionInitialisation(self):
        host= '127.0.0.1'
        port= 1234

        # Socket object creation
        try:
            self.server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        except socket.error:
            sys.exit()

        # Connection to port
        try:
            self.server_socket.connect((host, port))
        except socket.error:
            sys.exit()

