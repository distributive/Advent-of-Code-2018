# Answer: 1124

import re

file = open ("03.txt")

# Convert raw data
data = []
xMax = 0
yMax = 0

for line in file:
    l = int (re.search ("\d+(?=,)" , line).group ())
    t = int (re.search ("(?<=,)\d+", line).group ())
    w = int (re.search ("\d+(?=x)" , line).group ())
    h = int (re.search ("(?<=x)\d+", line).group ())
    if l + w > xMax:
        xMax = l + w
    if t + h > yMax:
        yMax = t + h
    data.append ((l, t, w, h))

# Create sheet matrix
sheet = []
for x in range (xMax):
    column = []
    for y in range (yMax):
        column.append (0)
    sheet.append (column)

# Apply the claims
for line in data:
    for x in range (line[0], line[0] + line[2]):
        for y in range (line[1], line[1] + line[3]):
            sheet[x][y] += 1

# Find the claim for which every square inch has exactly 1 use
i = 0
for line in data:
    i += 1
    valid = True
    for x in range (line[0], line[0] + line[2]):
        for y in range (line[1], line[1] + line[3]):
            if sheet[x][y] != 1:
                valid = False;
                break;
        if not valid:
            break;
    if valid:
        print (i)
        break;

file.close ()
