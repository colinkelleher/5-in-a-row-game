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
        message = json.dumps({"Player": self.username})
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

    def printGrid(self,grid,disc):
        for row in grid:
            return (" ".join(row))
        print("Please enter a number between 1-9 to place a %s", disc)

    def isGameOver(self,response):
        sys.exit()


    def gracefulExit(self):
        try:
            message = json.dumps({"Player": self.username, "nextPosition": "exit" })
            self.server_socket.send(message.encode())
            self.server_socket.close()
            sys.exit()
        except:
            sys.exit()

    def userMove(self,grid,disc):
        userInputtedVal = False
        self.printGrid(grid,disc)
        while not userInputtedVal :
            userInput = input("Enter Column: ")
            message = json.dumps({"Player": self.username, "nextPosition": userInput})
            self.server_socket.send(message.encode())
            self.response = json.loads(self.server_socket.recv(5000).decode())

            self.isGameOver(self.response)
            if self.response["status"] == "DISCONNECT":
                self.server_socket.close()
                sys.exit()

    def gameBody(self):
        while True:
            receivedData = self.server_socket.recv(5000).decode()
            self.response=json.loads(receivedData)
            self.isGameOver(self.response)

    def runClient(self):
        try:
            # get user to input their name
            self.inputUsername()
            # establish connection with server
            self.connectionInitialisation()
            # send username to server
            self.sendUsername()
            # play game
            self.gameBody()
            # exit once win/loose
            self.gracefulExit()
        except:
            sys.exit()

if __name__ == "__main__":
    Client().runClient()
