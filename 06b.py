# Answer: 42250

import math

file = open ("06.txt")

# Get data
points = {}
left   =  math.inf
right  = -math.inf
top    = -math.inf
bottom =  math.inf

for line in file:
    coords = line.split (",")
    x = int (coords[0])
    y = int (coords[1])
    points[(x, y)] = 0
    if x < left:
        left = x
    elif x > right:
        right = x
    if y > top:
        top = y
    elif y < bottom:
        bottom = y

# Gets the Manhattan distance between two points (x, y)
def distance (a, b):
    return abs (a[0] - b[0]) + abs (a[1] - b[1])

# Checks if a point lies on the edge of the bounded area
def onEdge (point):
    return point[0] == left or point[0] == right or point[1] == top or point[1] == bottom

# Count how many positions are closer than 10000 in total from every point
region = 0
for x in range (left, right+1):
    for y in range (bottom, top+1):
        distanceSum = 0
        for point in points.keys ():
            distanceSum += distance (point, (x, y))
        if distanceSum < 10000:
            region += 1

print (region)
file.close ()
