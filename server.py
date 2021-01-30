import sys
import socket
import threading
from threading import *
import json


class Server():

    def __init__(self, kwargs={}):
        self.serverSetup(kwargs)

    def serverSetup(self, kwargs={}):
        self.players = kwargs.get("players", [])
        self.columns = kwargs.get("columns", 9)
        self.rows = kwargs.get("rows", 6)
        self.grid = kwargs.get("grid",[])
        self.disc = kwargs.get("disc", {})
        self.lock = RLock()
        self.playerGo = kwargs.get("playerGo", "")
        self.playerWaiting = kwargs.get("playerWaiting", "")


    def newPlayer(self,player):
        if len(self.players) < 2:
            # preventing garbled output due to concurrent use of shared resource
            self.lock.acquire()
            self.players.append(player)
            self.lock.release()
            return True
        else:
            return False

    def getPlayerMove(self): # Switch between players
        if self.playerGo == self.players[0]:
            self.playerGo = self.players[1]
            self.playerWaiting =self.players[0]
        else:
            self.playerGo=self.players[0]
            self.playerWaiting  =self.players[1]

        jsonReady = {"status": "READY","grid": self.grid,"disc": self.disc[self.playerGo]}
        readyResponse = json.dumps(jsonReady)
        self.players[self.playerGo].send(readyResponse.encode())

        jsonWait = {"status":"WAIT", "grid":self.grid, "disc": self.disc[self.playerWaiting]}
        waitResponse = json.dumps(jsonWait)
        self.players[self.playerWaiting].send(waitResponse.encode())



    def createGrid(self):
        for number in range(self.rows):
            self.grid.append(["[ ]"] * self.columns)

    def checkResult(self):
        '''
        Check to see if there is 5 in a row
        '''
        sys.exit()

    def placeDisc(self, position):
        position = position - 1
        gridPosition = False

        sys.exit()


    def connectToPlayers(self, playerConnection):
        sys.exit()

    def playerConnection(self):
        sys.exit()

    def connectionInitialisation(self):
        host= '127.0.0.1'
        port= 1234
        # Socket object creation
        try:
            self.client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        except socket.error:
            sys.exit()
        # Connection to port
        try:
            self.client_socket.bind((host,port))
        except socket.error:
            sys.exit()
        self.client_socket.listen(5)

    def runServer(self):
        self.serverSetup()


if __name__ == "__main__":
    Server().runServer()
