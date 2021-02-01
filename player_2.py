import socket
import sys
import json


class Client():

    def __init__(self, username=''):
        self.username = username

    def inputUsername(self):
        self.username = input("Please enter your username: ")

    def connectionInitialisation(self):
        host = '127.0.0.1'
        port = 1337
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
            sys.exit()

        try:
            self.server_socket.connect((host, port))
        except socket.error:
            sys.exit()

    def sendUsername(self):
        client_message = json.dumps({"newPlayer": self.username})
        self.server_socket.send(client_message.encode())
        userResponse = json.loads(self.server_socket.recv(4096).decode())
        if userResponse["msgStatus"] == "JOIN":
            print("Welcome to 5-in-a-Row")
        elif userResponse["msgStatus"] == "FULL":
            print("We already have two players")
            self.server_socket.close()
            sys.exit()

    def game(self):
        while True:
            self.response = json.loads(self.server_socket.recv(4096).decode())

            self.isGameOver(self.response)

            while self.response["msgStatus"] == "PLAYERWAITING":
                print("Waiting for another player to join....")
                self.response = json.loads(self.server_socket.recv(4096).decode())

            if self.response["msgStatus"] == "WAIT":
                print("It is your opponent's turn. Please Wait!")

            if self.response["msgStatus"] == "READY":
                if ("grid" in self.response.keys() and "disc" in self.response.keys()):
                    grid = self.response["grid"]
                    disc = self.response["disc"]
                    self.userMove(grid, disc)

                if self.response["msgStatus"] == "WAIT":
                    print("It is your opponent's turn. Please Wait!")

    def userMove(self, grid, disc):
        trueInput = False
        self.printGrid(grid, disc)
        while not trueInput:
            inputVal = input("Enter Column: ")

            message = json.dumps({"currentPlayer": self.username, "nextMove": inputVal})
            self.server_socket.send(message.encode())
            self.response = json.loads(self.server_socket.recv(4096).decode())

            self.isGameOver(self.response)
            if self.response["msgStatus"] == "DISCONNECT":
                self.server_socket.close()
                sys.exit()
            if self.response["msgStatus"] == "ERROR":
                print("invalid command. Please try again")
                trueInput = False
            elif self.response["msgStatus"] == "COLFULL":
                print("column is full")
                trueInput = False
            else:
                trueInput = True

    def printGrid(self, grid, disc):
        for row in grid:
            print(" ".join(row))
        print("Please enter a number between 1-9 to place an %s" % disc)

    def isGameOver(self, response):
        if response["msgStatus"] == "DISCONNECT":
            print("Server error. Have to disconnect")
            self.gracefulExit()

        if response["msgStatus"] == "WIN":
            print(f"Congratulations {self.username}! You won!")
            self.gracefulExit()

        if response["msgStatus"] == "LOSS":
            print(f"Sorry {self.username}. You lost!")
            self.gracefulExit()

        if response["msgStatus"] == "DRAW":
            print(f"The game ended in a draw {self.username}")
            self.gracefulExit()

    def gracefulExit(self):
        try:
            message = json.dumps({"currentPlayer": self.username, "nextMove": "exit"})
            self.server_socket.send(message.encode())
            self.server_socket.close()
            sys.exit()
        except:
            sys.exit()

    def playerRun(self):
        try:
            self.inputUsername()
            self.connectionInitialisation()
            self.sendUsername()
            self.game()
            self.gracefulExit()
        except:
            self.gracefulExit()


if __name__ == "__main__":
    Client().playerRun()