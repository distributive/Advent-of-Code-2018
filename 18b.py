# Answer: 169024

file = open ("18.txt")

# Read initial setup
grid = []
for line in file:
    grid.append ([c for c in line if c != "\n"])
file.close ()

limit = 1000000000
pastGrids = [grid]

# Main loop
t = 0
while t < limit:
    t += 1
##    display ()
    newGrid = []
    for y in range (len (grid)):
        newGrid.append ([])
        for x in range (len (grid[y])):
            adjacent = [grid[yPos][xPos] for xPos in range (max (0, x-1), min (len (grid[y]), x+2)) for yPos in range (max (0, y-1), min (len (grid), y+2)) if (xPos,yPos) != (x,y)]
            if grid[y][x] == "." and adjacent.count ("|") >= 3:
                newGrid[y].append ("|")
            elif grid[y][x] == "|" and adjacent.count ("#") >= 3:
                newGrid[y].append ("#")
            elif grid[y][x] == "#" and (adjacent.count ("|") < 1 or adjacent.count ("#") < 1):
                newGrid[y].append (".")
            else:
                newGrid[y].append (grid[y][x])

    if newGrid in pastGrids:
        index = pastGrids.index (newGrid)
        timeRemaining = (limit - t) % (t - index)
        grid = pastGrids[index+timeRemaining]
        break
    grid = newGrid
    pastGrids.append (grid)

print (sum ([row.count ("|") for row in grid]) * sum ([row.count ("#") for row in grid]))
