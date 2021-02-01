from server import Server
from player_1 import Client
import unittest


class testPlayer (unittest.TestCase):

    def test_newPlayer(self):
        server = Server()
        server.newPlayer("Colin")
        self.assertTrue(server.players == ["Colin"])

    def test_newPlayer1(self):
        server = Server()
        server.newPlayer("Colin")
        self.assertFalse(server.players == ["Genesys"])

class testgrid(unittest.TestCase):


    def test_GridSetup(self):
        server = Server()
        server.createGrid()
        self.assertTrue(server.grid == [
        ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
        ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
        ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
        ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
        ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
        ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]']
    ])

    def test_GridSetup1(self):
        server = Server()
        server.createGrid()
        self.assertFalse(server.grid == [
        ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
        ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
        ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
        ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
        ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
        ['[ ]', '[ ]', '[ ]', '[ ]']
    ])

class testResults(unittest.TestCase):
    def test_Draw(self):
        server = Server()
        server.kwargs={"playerGo": "Colin","disc": {"Colin": "O"},"grid": [
                    ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
                    ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
                    ['[X]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
                    ['[X]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
                    ['[X]', '[ ]', '[ ]', '[O]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
                    ['[X]', '[ ]', '[ ]', '[O]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]']
                ]
            }
        self.assertFalse(server.isDraw == False)

class ClientTests(unittest.TestCase):
    def test_username(self):
        client = Client()
        username = client.inputUsername()
        self.assertFalse(username== "jk")


if __name__ == '__main__':
    testPlayer()
    testgrid()
    testResults()


