# Answer: 570

import re

file = open ("16.txt")

# Read data
instructions = []
lineCount = 0
for line in file:
    if lineCount == 0:
        if line[0] != "B":
            break
        instructions.append ([list (map (int, re.search ("\[.*\]", line).group ()[1:-1].split (",")))])
    elif lineCount == 1:
        instructions[-1].append (list (map (int, line[:-1].split (" "))))
    elif lineCount == 2:
        instructions[-1].append (list (map (int, re.search ("\[.*\]", line).group ()[1:-1].split (","))))
    lineCount = (lineCount + 1) % 4
file.close ()

# Run tests
threes = []

for ins in instructions:
    count = 0
    # addr
    if ins[0][ins[1][1]] + ins[0][ins[1][2]] == ins[2][ins[1][3]]:
        count += 1
    # addi
    if ins[0][ins[1][1]] + ins[1][2] == ins[2][ins[1][3]]:
        count += 1
    # mulr
    if ins[0][ins[1][1]] * ins[0][ins[1][2]] == ins[2][ins[1][3]]:
        count += 1
    # muli
    if ins[0][ins[1][1]] * ins[1][2] == ins[2][ins[1][3]]:
        count += 1
    # banr
    if ins[0][ins[1][1]] & ins[0][ins[1][2]] == ins[2][ins[1][3]]:
        count += 1
    # bani
    if ins[0][ins[1][1]] & ins[1][2] == ins[2][ins[1][3]]:
        count += 1
    # borr
    if ins[0][ins[1][1]] | ins[0][ins[1][2]] == ins[2][ins[1][3]]:
        count += 1
    # bori
    if ins[0][ins[1][1]] | ins[1][2] == ins[2][ins[1][3]]:
        count += 1
    # setr
    if ins[0][ins[1][1]] == ins[2][ins[1][3]]:
        count += 1
    # seti
    if ins[1][1] == ins[2][ins[1][3]]:
        count += 1
    # gtir
    if (ins[1][1] > ins[0][ins[1][2]] and ins[2][ins[1][3]] == 1 or ins[2][ins[1][3]] == 0):
        count += 1
    # gtri
    if (ins[0][ins[1][1]] > ins[1][2] and ins[2][ins[1][3]] == 1 or ins[2][ins[1][3]] == 0):
        count += 1
    # gtrr
    if (ins[0][ins[1][1]] > ins[0][ins[1][2]] and ins[2][ins[1][3]] == 1 or ins[2][ins[1][3]] == 0):
        count += 1
    # eqir
    if (ins[1][1] == ins[0][ins[1][2]] and ins[2][ins[1][3]] == 1 or ins[2][ins[1][3]] == 0):
        count += 1
    # eqri
    if (ins[0][ins[1][1]] == ins[1][2] and ins[2][ins[1][3]] == 1 or ins[2][ins[1][3]] == 0):
        count += 1
    # eqrr
    if (ins[0][ins[1][1]] == ins[0][ins[1][2]] and ins[2][ins[1][3]] == 1 or ins[2][ins[1][3]] == 0):
        count += 1

    if count >= 3:
        threes.append (ins)

print (len (threes))
