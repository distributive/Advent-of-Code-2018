# Answer: 3189426841
# It took like 12 hours

import re

file = open ("9.txt")
line = file.readline ()

playerCount = int (re.search ("\d*(?= pl)", line).group ())
marbleCount = int (re.search ("\d*(?= po)", line).group ()) * 100

# Set up score table
players = {}
for player in range (playerCount):
    players[player + 1] = 0

# Play the game
marbles = [0]
currentIndex = 0
currentPlayer = 1

for i in range (1, marbleCount + 1):
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
