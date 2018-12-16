# Answer: 503

import re

file = open ("16.txt")

# Read examples
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

# Read program
program = []
for line in file:
    if len (line) > 1:
        program.append (list (map (int, line.split (" "))))

file.close ()

# Run tests
possibilities = [[i for i in range (16)] for i in range (16)] # [opcode] = possible instructions
for ins in instructions:
    count = 0
    flags = [False]*16
    # addr
    if ins[0][ins[1][1]] + ins[0][ins[1][2]] == ins[2][ins[1][3]]:
        count += 1
        flags[0] = True
    # addi
    if ins[0][ins[1][1]] + ins[1][2] == ins[2][ins[1][3]]:
        count += 1
        flags[1] = True
    # mulr
    if ins[0][ins[1][1]] * ins[0][ins[1][2]] == ins[2][ins[1][3]]:
        count += 1
        flags[2] = True
    # muli
    if ins[0][ins[1][1]] * ins[1][2] == ins[2][ins[1][3]]:
        count += 1
        flags[3] = True
    # banr
    if ins[0][ins[1][1]] & ins[0][ins[1][2]] == ins[2][ins[1][3]]:
        count += 1
        flags[4] = True
    # bani
    if ins[0][ins[1][1]] & ins[1][2] == ins[2][ins[1][3]]:
        count += 1
        flags[5] = True
    # borr
    if ins[0][ins[1][1]] | ins[0][ins[1][2]] == ins[2][ins[1][3]]:
        count += 1
        flags[6] = True
    # bori
    if ins[0][ins[1][1]] | ins[1][2] == ins[2][ins[1][3]]:
        count += 1
        flags[7] = True
    # setr
    if ins[0][ins[1][1]] == ins[2][ins[1][3]]:
        count += 1
        flags[8] = True
    # seti
    if ins[1][1] == ins[2][ins[1][3]]:
        count += 1
        flags[9] = True
    # gtir
    if ins[1][1] > ins[0][ins[1][2]] and ins[2][ins[1][3]] == 1 or ins[2][ins[1][3]] == 0:
        count += 1
        flags[10] = True
    # gtri
    if ins[0][ins[1][1]] > ins[1][2] and ins[2][ins[1][3]] == 1 or ins[2][ins[1][3]] == 0:
        count += 1
        flags[11] = True
    # gtrr
    if ins[0][ins[1][1]] > ins[0][ins[1][2]] and ins[2][ins[1][3]] == 1 or ins[2][ins[1][3]] == 0:
        count += 1
        flags[12] = True
    # eqir
    if ins[1][1] == ins[0][ins[1][2]] and ins[2][ins[1][3]] == 1 or ins[2][ins[1][3]] == 0:
        count += 1
        flags[13] = True
    # eqri
    if ins[0][ins[1][1]] == ins[1][2] and ins[2][ins[1][3]] == 1 or ins[2][ins[1][3]] == 0:
        count += 1
        flags[14] = True
    # eqrr
    if ins[0][ins[1][1]] == ins[0][ins[1][2]] and ins[2][ins[1][3]] == 1 or ins[2][ins[1][3]] == 0:
        count += 1
        flags[15] = True

    # Filter out possibilities
    opcode = ins[1][0]
    for i in possibilities[opcode]:
        if not flags[i]:
            possibilities[opcode].remove (i)

# Reduce possibilities
while True:
    check = sum (map (sum, possibilities))
    
    for i in range (len (possibilities)):
        if len (possibilities[i]) == 1:
            for j in range (len (possibilities)):
                if i != j and possibilities[i][0] in possibilities[j]:
                    possibilities[j].remove (possibilities[i][0])
    
    possibilities = [[i for i in range (16) if j in possibilities[i]] for j in range (16)]

    for i in range (len (possibilities)):
        if len (possibilities[i]) == 1:
            for j in range (len (possibilities)):
                if i != j and possibilities[i][0] in possibilities[j]:
                    possibilities[j].remove (possibilities[i][0])
    
    possibilities = [[i for i in range (16) if j in possibilities[i]] for j in range (16)]
    
    if check == sum (map (sum, possibilities)):
        if any (map (lambda x : len (x) > 1, possibilities)):
            for i in range (len (possibilities)):
                if len (possibilities[i]) > 1:
                    # Guess which opcode ambiguous cases resolve to
                    # This method works for the given input (opcodes 2 and 3 have to be guessed)
                    possibilities[i] = possibilities[i][0:1]
                    break
        else:
            break

# Run program
reg = [0]*4
for cmd in program:
    operation = possibilities[cmd[0]][0]
    if (len (possibilities[cmd[0]]) > 1):
        print (cmd)
    
    # addr
    if operation == 0:
        reg[cmd[3]] = reg[cmd[1]] + reg[cmd[2]]
    # addi
    elif operation == 1:
        reg[cmd[3]] = reg[cmd[1]] + cmd[2]
    # mulr
    elif operation == 2:
        reg[cmd[3]] = reg[cmd[1]] * reg[cmd[2]]
    # muli
    elif operation == 3:
        reg[cmd[3]] = reg[cmd[1]] * cmd[2]
    # banr
    elif operation == 4:
        reg[cmd[3]] = reg[cmd[1]] & reg[cmd[2]]
    # bani
    elif operation == 5:
        reg[cmd[3]] = reg[cmd[1]] & cmd[2]
    # borr
    elif operation == 6:
        reg[cmd[3]] = reg[cmd[1]] | reg[cmd[2]]
    # bori
    elif operation == 7:
        reg[cmd[3]] = reg[cmd[1]] | cmd[2]
    # setr
    elif operation == 8:
        reg[cmd[3]] = reg[cmd[1]]
    # seti
    elif operation == 9:
        reg[cmd[3]] = cmd[1]
    # gtir
    elif operation == 10:
        reg[cmd[3]] = 1 if cmd[1] > reg[cmd[2]] else 0
    # gtri
    elif operation == 11:
        reg[cmd[3]] = 1 if reg[cmd[1]] > cmd[2] else 0
    # gtrr
    elif operation == 12:
        reg[cmd[3]] = 1 if reg[cmd[1]] > reg[cmd[2]] else 0
    # eqir
    elif operation == 13:
        reg[cmd[3]] = 1 if cmd[1] == reg[cmd[2]] else 0
    # eqri
    elif operation == 14:
        reg[cmd[3]] = 1 if reg[cmd[1]] == cmd[2] else 0
    # eqrr
    else:
        reg[cmd[3]] = 1 if reg[cmd[1]] == reg[cmd[2]] else 0

print (reg[0])
