from server import Server
from player_1 import Client
import unittest


class testSetup (unittest.TestCase):

    def test_newPlayer(self):
        server = Server()
        server.newPlayer("Colin")
        self.assertTrue(server.players == ["Colin"])

    def test_newPlayer1(self):
        server = Server()
        server.newPlayer("Colin")
        self.assertFalse(server.players == ["Genesys"])

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





if __name__ == '__main__':
    unittest.main()


