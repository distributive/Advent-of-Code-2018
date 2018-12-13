# Answer: 243,34
# Assumes the serial number (puzzle input) will be positive

import math

file = open ("11.txt")
serial = int (file.readline ())
file.close ()

# Create grid of power levels
grid = [[int (str (1000 + ((x + 10) * y + serial) * (x + 10))[-3]) - 5 for y in range (1, 301)] for x in range (1, 301)]

# Find the maximum power
maxCoords = (0, 0)
maxPower = -math.inf
for x in range (0, 298):
    for y in range (0, 298):
        newPower = sum (grid[x][y:y+3]) + sum (grid[x+1][y:y+3]) + sum (grid[x+2][y:y+3])
        if newPower > maxPower:
            maxPower = newPower
            maxCoords = (x+1, y+1)

print (str (maxCoords[0]) + "," + str (maxCoords[1]))

