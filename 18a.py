# Answer: 583426

file = open ("18.txt")

# Read initial setup
grid = []
for line in file:
    grid.append ([c for c in line if c != "\n"])
file.close ()

##def display ():
##    s = ""
##    for line in grid:
##        for char in line:
##            s += char
##        s += "\n"
##    s += "\n"
##    print (s)

# Main loop
for t in range (10):
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
    grid = newGrid

##display ()

print (sum ([row.count ("|") for row in grid]) * sum ([row.count ("#") for row in grid]))
