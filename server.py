import sys
import socket


class Server():

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