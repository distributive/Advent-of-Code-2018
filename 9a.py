# Answer: 384288

import re

file = open ("9.txt")
line = file.readline ()

playerCount = int (re.search ("\d*(?= pl)", line).group ())
marbleCount = int (re.search ("\d*(?= po)", line).group ())

# Set up score table
players = {}
for player in range (playerCount):
    players[player + 1] = 0

# Play the game
marbles = [0]
currentIndex = 0
currentPlayer = 1

for i in range (1, marbleCount):
    if i % 23 != 0:
        currentIndex = (currentIndex + 2) % len (marbles)
        marbles.insert (currentIndex, i)
    else:
        currentIndex = (currentIndex - 7) % len (marbles)
        players[player] += i + marbles.pop (currentIndex)

    player += 1
    if player > playerCount:
        player = 1

print (max (players.values ()))
file.close ()
