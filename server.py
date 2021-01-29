import sys
import socket


class Server():

    def __init__(self, kwargs={}):
        self.serverSetup(kwargs)

    def serverSetup(self, kwargs={}):
        self.players = kwargs.get("players", [])
        self.columns = kwargs.get("columns", 9)
        self.rows = kwargs.get("rows", 6)
        self.grid = kwargs.get("grid",[])
        self.disc = kwargs.get("disc", {})

    def createBoard(self):
        for number in range(self.rows):
            self.grid.append(["[ ]"] * self.columns)

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
        sys.exit()


if __name__ == "__main__":
    Server().runServer()
