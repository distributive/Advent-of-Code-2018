# Answer: 10521
# The answer was already outputted in part a but this removes the visualisation

import re
import math

file = open ("10.txt")

# Read in all points
points = []

for line in file:
    x  = int (re.search ("(?<=n=<)[ -]\d*", line).group ())
    y  = int (re.search ("[ -]\d*(?=> v)" , line).group ())
    vx = int (re.search ("(?<=y=<)[ -]\d*", line).group ())
    vy = int (re.search ("[ -]\d*(?=>$)"  , line).group ())
    points.append (((x, y), (vx, vy)))

# Animate the points
t = 0
grids = []
gridRange = math.inf
while True:
    # Store data on the grid in its current state
    xBounds = (math.inf, -math.inf)
    yBounds = (math.inf, -math.inf)
    grid = set ()
    for point in points:
        x = point[0][0] + t*point[1][0]
        y = point[0][1] + t*point[1][1]
        xBounds = (min (x, xBounds[0]), max (x, xBounds[1]))
        yBounds = (min (y, yBounds[0]), max (y, yBounds[1]))
        grid.add ((x, y))
    grids.append ((grid, xBounds, yBounds))

    # Check if the grid is notably small (indicating convergence on a message)
    newGridRange = xBounds[1] - xBounds[0] + yBounds[1] - yBounds[0]
    if newGridRange < gridRange:
        gridRange = newGridRange
    else:
        print (t-1)
        break
    t += 1

file.close ()
