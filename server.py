import sys
import socket
import threading
import time 
from threading import *
import json


class Server():

    def __init__(self, kwargs={}):
        self.serverSetup(kwargs)

    def serverSetup(self, kwargs={}):
        self.players = kwargs.get("players", [])
        self.columns = kwargs.get("columns", 9)
        self.gameHasStarted = kwargs.get("gameHasStarted", False)
        self.colFull = False
        self.rows = kwargs.get("rows", 6)
        self.grid = kwargs.get("grid", [])
        self.disc = kwargs.get("disc", {})
        self.lock=RLock()
        self.playerGo = kwargs.get("playerGo", "")
        self.playerWaiting = kwargs.get("playerWaiting", "")
        self.connections = kwargs.get("connections", {})

    def newPlayer(self, player):
        if len(self.players) < 2:
            self.lock.acquire()
            self.players.append(player)
            self.lock.release()
            return True
        else:
            return False


    def getPlayerMove(self):
        if self.playerGo==self.players[0]:
            self.playerGo=self.players[1]
            self.playerWaiting=self.players[0]
        else:
            self.playerGo=self.players[0]
            self.playerWaiting=self.players[1]

        jsonReady = {"msgStatus": "READY","grid": self.grid,"disc": self.disc[self.playerGo]}
        response = json.dumps(jsonReady)
        self.connections[self.playerGo].send(response.encode())

        jsonWait = {"msgStatus": "WAIT","grid": self.grid,"disc": self.disc[self.playerWaiting]}
        response = json.dumps(jsonWait)
        self.connections[self.playerWaiting].send(response.encode())

    def createGrid(self):
        for number in range(self.rows):
            self.grid.append(["[ ]"] * self.columns)

    def connectionInitialisation(self):
        host='127.0.0.1'
        port=1337
        try:
            self.playerSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        except socket.error:
            sys.exit()
        self.playerSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

        try:
            self.playerSocket.bind((host,port))
        except socket.error:
            sys.exit()
        self.playerSocket.listen(5)

    def isDraw(self):
        if "[ ]" not in self.grid[0]:
            if not self.isWinner():
                return True
        return False

    def connectToPlayers(self, playerConnection):
        while True:
            try:
                connect = playerConnection.recv(4096).decode()
                if not connect:
                    break
                connect = json.loads(connect)
                if "currentPlayer" in connect.keys():
                    self.currentPlayer = connect["currentPlayer"]

                if "newPlayer" in connect.keys():
                    self.currentPlayer = connect["newPlayer"]
                    if self.newPlayer(connect["newPlayer"]):
                        client_response = json.dumps({"msgStatus": "JOIN"})
                        playerConnection.send(client_response.encode())
                        self.lock.acquire()
                        self.connections[self.currentPlayer] = playerConnection
                        self.lock.release()
                        while len(self.players) == 1:
                            response = json.dumps({"msgStatus": "PLAYERWAITING"})
                            playerConnection.send(response.encode())
                            time.sleep(5)

                        if len(self.players) == 2 and not self.gameHasStarted:
                            self.playerGo = self.players[0]
                            self.disc[self.players[0]] = 'X'
                            self.playerWaiting = self.players[1]
                            self.disc[self.players[1]] = 'O'
                            self.createGrid()
                            self.getPlayerMove()
                            self.gameHasStarted = True
                    else:
                        response = json.dumps({"msgStatus": "FULL"})
                        playerConnection.send(response.encode())
                elif "nextMove" in connect.keys():
                    position = connect["nextMove"]

                    if position.isdigit() and len(position) == 1 and int(position) <= self.columns:
                        self.placeDisc(int(position))
                        if not self.colFull:
                            self.getPlayerMove()
                        else:
                            self.colFull = False
                    elif position == "exit":
                        if self.currentPlayer in self.players:
                            self.lock.acquire()
                            self.players.remove(self.currentPlayer)
                            self.lock.release()
                        response = json.dumps({"msgStatus": "DISCONNECT"})
                        playerConnection.send(response.encode())
                        playerConnection.close()
                        self.disconnectPlayers()
                        break
                    else:
                        response = json.dumps({"msgStatus": "ERROR"})
                        playerConnection.send(response.encode())
            except:
                self.disconnectPlayers()

    def placeDisc(self, position):
        position = position -1
        gridPosition = False
        for i in range(self.rows -1 , -1, -1):
            if self.grid[i][position] == "[ ]" and not gridPosition:
                self.grid[i][position] = f"[{self.disc[self.playerGo]}]"
                gridPosition = True
        if not gridPosition:
            self.colFull = True
            colResp = json.dumps({"msgStatus": "COLFULL"})
            self.connections[self.playerGo].send(colResp.encode())
        if self.isWinner():
            response = json.dumps({"msgStatus": "WIN"})
            self.connections[self.playerGo].send(response.encode())
            response = json.dumps({"msgStatus": "LOSS"})
            self.connections[self.playerWaiting].send(response.encode())
        if self.isDraw():
            response= json.dumps({"msgStatus": "DRAW"})
            self.connections[self.playerGo].send(response.encode())
            self.connections[self.playerWaiting].send(response.encode())

    def isWinner(self):
        for y in range(self.columns):
            for x in range(self.rows - 4):
                if (self.disc[self.playerGo] in self.grid[x][y] and
                        # increasing the row number
                        self.disc[self.playerGo] in self.grid[x+1][y] and
                        self.disc[self.playerGo] in self.grid[x+2][y] and
                        self.disc[self.playerGo] in self.grid[x+3][y] and
                        self.disc[self.playerGo] in self.grid[x+4][y]):
                    return True

        for x in range(self.rows - 4):
            for y in range(self.columns - 4):
                # increasing the row and column number
                if (self.disc[self.playerGo] in self.grid[x][y] and
                        self.disc[self.playerGo] in self.grid[x + 1][y + 1] and
                        self.disc[self.playerGo] in self.grid[x + 2][y + 2] and
                        self.disc[self.playerGo] in self.grid[x + 3][y + 3] and
                        self.disc[self.playerGo] in self.grid[x + 4][y + 4]):
                    return True

        for x in range(self.rows):
            for y in range(self.columns - 4):
                # increasing the column number
                if (self.disc[self.playerGo] in self.grid[x][y] and
                        self.disc[self.playerGo] in self.grid[x][y+1] and
                        self.disc[self.playerGo] in self.grid[x][y+2] and
                        self.disc[self.playerGo] in self.grid[x][y+3] and
                        self.disc[self.playerGo] in self.grid[x][y+4]):
                    return True

        for x in range(self.rows - 4):
            for y in range(4, self.columns):
                if (self.disc[self.playerGo] in self.grid[x][y] and
                        # increasing the row number and decreasing the column number
                        self.disc[self.playerGo] in self.grid[x+1][y-1] and
                        self.disc[self.playerGo] in self.grid[x+2][y-2] and
                        self.disc[self.playerGo] in self.grid[x+3][y-3] and
                        self.disc[self.playerGo] in self.grid[x+4][y-4]):
                    return True
        return False

    def disconnectPlayers(self):
        for player in self.players:
            try:
                self.players.remove(player)
                ready_response = json.dumps({"msgStatus": "DISCONNECT"})
                self.connections[player].send(ready_response.encode())
            except:
                sys.exit()
        self.serverSetup()

    def runServer(self):
        self.connectionInitialisation()
        while True:
            conn, addr = self.playerSocket.accept()
            threads = threading.Thread(target=self.connectToPlayers,args=(conn,))
            threads.start()

if __name__ == "__main__":
    Server().runServer()