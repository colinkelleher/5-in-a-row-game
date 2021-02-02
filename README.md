# 5-in-a-Row
## Colin Kelleher
<p>5-in-a-Row, a variation of the famous Connect Four game, is a two-player connection game in which the players first choose a color and then take turns dropping colored discs from the top into a nine-column, six-row vertically suspended grid. The pieces fall straight down, occupying the next available space within the column. The objective of the game is to be the first to form a horizontal, vertical, or diagonal line of five of one's own discs.</p>

### Specifications
- [x] The server application holds the state and business logic of the game, receiving the movements from the players and deciding whether a player has won, or the game is over. The state of the game, and who's turn it is, will be returned to the client upon request. The communication between the clients and the server should be over HTTP.
- [x] The server, upon start, waits for the two players to connect. If one of the players disconnects, the game is over. 
- [x] The client prompts the player to enter their name upon start, and displays whether it's waiting for a 2nd player, or the game can start.
- [x] On each turn, the client displays the state of the board and prompts the corresponding player for input or displays that it's waiting for the other player's input.
- [x] The client receives the input from the player from the standard input (stdin).
- [x] The client displays when the game is over, and the name of the winner.

- [x] Testing

### Colin's Notes

### How to run the game

1. Run your server -> 'python3 server.py'
2. Run player1 -> 'python3 player1.py' and enter your name as prompted
3. Run player2 -> 'python3 player2.py' and enter your name as prompted
4. Game is now running!
