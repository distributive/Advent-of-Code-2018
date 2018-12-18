# Answer: 31412

import math
import re

file = open ("17.txt")

# Read input
grid = set ()
for line in file:
    x = re.search ("(?<=x=)[\d\.]*", line).group ()
    y = re.search ("(?<=y=)[\d\.]*", line).group ()
    if line[0] == "x":
        yRange = y.split (".")
        for i in range (int (yRange[0]), int (yRange[2])+1):
            grid.add ((int (x), i))
    else:
        xRange = x.split (".")
        for i in range (int (xRange[0]), int (xRange[2])+1):
            grid.add ((i, int (y)))
file.close ()

# Find min and max y values
sortedGrid = sorted (grid, key=lambda c : c[1])
minY = sortedGrid[0][1]
maxY = sortedGrid[-1][1]

# Find min and max y values
sortedGrid = sorted (grid, key=lambda c : c[0])
minX = sortedGrid[0][0] - 1
maxX = sortedGrid[-1][0] + 1

# Get the horizontal bounds on a given position
# Each side returned as (x, y, doesLeak)
# Assumes any given coordinate will be bounded within minX and maxX
def horizontalBounds (pos):
    for x in range (pos[0], maxX+1):
        if (x, pos[1]+1) not in grid:
            rightBarrier = (x, pos[1], True)
            break
        elif (x+1, pos[1]) in grid:
            rightBarrier = (x, pos[1], False)
            break
    for x in range (pos[0], minX-1, -1):
        if (x, pos[1]+1) not in grid:
            leftBarrier = (x, pos[1], True)
            break
        elif (x-1, pos[1]) in grid:
            leftBarrier = (x, pos[1], False)
            break
    return (leftBarrier, rightBarrier)

# Set spring location
streams = [[500, minY]]
streamGrid = set ()
oldLen = len (grid)

# Pour water
while len (streams):
    newStreams = []
    removeStreams = []
    for stream in streams:
        streamGrid.add ((stream[0], stream[1]))
        # Extend stream until hits clay or depth limit
        while stream[1] < maxY and (stream[0], stream[1] + 1) not in grid:
            stream[1] += 1
            if stream[1] >= minY:
                streamGrid.add ((stream[0], stream[1]))
        # If hit depth limit
        if stream[1] >= maxY:
            removeStreams.append (stream)
        # If hit clay
        else:
            bounds = horizontalBounds ((stream[0], stream[1]))
            if bounds[0][2] or bounds[1][2]:
                removeStreams.append (stream)
                if bounds[0][2]:
                    newStreams.append ([bounds[0][0], bounds[0][1]])
                if bounds[1][2]:
                    newStreams.append ([bounds[1][0], bounds[1][1]])
                streamGrid.update ([(x, stream[1]) for x in range (bounds[0][0], bounds[1][0]+1)])
                break
            else:
                grid.update ([(x, stream[1]) for x in range (bounds[0][0], bounds[1][0]+1)])
                stream[1] -= 1
            
    # Update list of streams
    streams = [stream for stream in streams if stream not in removeStreams]
    streams.extend (newStreams)

# Add coordinates covered by streams
grid.update (streamGrid)

print (len (grid) - oldLen)
