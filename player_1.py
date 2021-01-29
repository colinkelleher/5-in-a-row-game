import socket
import sys
import json

class Client():

    def __init__(self, username=''):
        self.username = username

    def inputUsername(self):
        self.username = input("Please enter your username: ")

    def sendUsername(self):
        '''
        Register the username entered by the user with the server
        '''
        message = json.dumps({"newPlayer": self.username})
        encodedMessage = message.encode()
        self.server_socket.send(encodedMessage)
        serverResponse = json.load(self.server_socket.recv(10000).decode())
        if serverResponse["msgStatus"] == "200":
            print("Welcome to 5-in-a-Row %s", serverResponse)
        else:
            self.server_socket.close()
            sys.exit()

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

    def printBoard(self,grid,disc):
        for row in grid:
            print(" ".join(row))
        print("Please enter a number between 1-9 to place a %s", disc)

    def userMove(self,grid,disc):
        userInputtedVal = False
        self.printBoard(grid,disc)
        while not userInputtedVal :
            userInput = input("Enter Column: ")

    def runClient(self):
        try:
            self.inputUsername()
            self.connectionInitialisation()
        except:
            sys.exit()

if __name__ == "__main__":
    Client().runClient()
