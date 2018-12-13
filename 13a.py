# Answer: 58,93

file = open ("13.txt")

# Cart class
class Cart ():
    directions = ("^", ">", "v", "<")
    corners = {
        "/" : {"^":">", ">":"^", "v":"<", "<":"v"},
        "\\": {"v":">", ">":"v", "^":"<", "<":"^"}
        }
    
    def __init__ (self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.intersection = 0

    def move (self):
        if self.direction == ">":
            self.x += 1
        elif self.direction == "<":
            self.x -= 1
        elif self.direction == "^":
            self.y -= 1
        else:
            self.y += 1

        char = track[(self.x, self.y)] if (self.x, self.y) in track.keys () else ""
        if char == "+":
            self.direction = self.directions[(self.directions.index (self.direction) + self.intersection - 1) % 4]
            self.intersection = (self.intersection + 1) % 3
        elif char:
            self.direction = self.corners[char][self.direction]

# Set up map of the tracks
track = {}
carts = []

y = 0
for line in file:
    x = 0
    for char in line:
        if char in Cart.directions:
            carts.append (Cart (x, y, char))
        elif char in ("\\", "/", "+"):
            track[(x,y)] = char
        x += 1
    y += 1

# Move carts
collision = ()

while not collision:
    carts = sorted (carts, key=lambda cart : float (str (cart.y) + "." + str (cart.x)))
    for c in carts:
        c.move ()
        for d in carts:
            if c != d and c.x == d.x and c.y == d.y:
                collision = (c.x, c.y)
                break
        if collision:
            break

##    # Draw state of the track
##    s = ""
##    for y in range (len (grid)):
##        for x in range (len (grid[y])):
##            c = [c for c in carts if c.x == x and c.y == y]
##            s += c[0].direction if c else grid[y][x]
##    print (s)

print (str (collision[0]) + "," + str (collision[1]))
file.close ()
