# Answer: 1728

import re

file = open ("19.txt")

# Read data
ir = int (re.search ("\d", file.readline ()).group ())

instructions = []
for line in file:
    instructions.append (line)

file.close ()

# Run program
reg = [0]*6
while reg[ir] >= 0 and reg[ir] < len (instructions):
    cmd = instructions[reg[ir]].split (" ")
    cmd = [cmd[0], int (cmd[1]), int (cmd[2]), int (cmd[3])]
    ins = cmd[0]
    
    # addr
    if ins == "addr":
        reg[cmd[3]] = reg[cmd[1]] + reg[cmd[2]]
    # addi
    elif ins == "addi":
        reg[cmd[3]] = reg[cmd[1]] + cmd[2]
    # mulr
    elif ins == "mulr":
        reg[cmd[3]] = reg[cmd[1]] * reg[cmd[2]]
    # muli
    elif ins == "muli":
        reg[cmd[3]] = reg[cmd[1]] * cmd[2]
    # banr
    elif ins == "banr":
        reg[cmd[3]] = reg[cmd[1]] & reg[cmd[2]]
    # bani
    elif ins == "bani":
        reg[cmd[3]] = reg[cmd[1]] & cmd[2]
    # borr
    elif ins == "borr":
        reg[cmd[3]] = reg[cmd[1]] | reg[cmd[2]]
    # bori
    elif ins == "bori":
        reg[cmd[3]] = reg[cmd[1]] | cmd[2]
    # setr
    elif ins == "setr":
        reg[cmd[3]] = reg[cmd[1]]
    # seti
    elif ins == "seti":
        reg[cmd[3]] = cmd[1]
    # gtir
    elif ins == "gtir":
        reg[cmd[3]] = 1 if cmd[1] > reg[cmd[2]] else 0
    # gtri
    elif ins == "gtri":
        reg[cmd[3]] = 1 if reg[cmd[1]] > cmd[2] else 0
    # gtrr
    elif ins == "gtrr":
        reg[cmd[3]] = 1 if reg[cmd[1]] > reg[cmd[2]] else 0
    # eqir
    elif ins == "eqir":
        reg[cmd[3]] = 1 if cmd[1] == reg[cmd[2]] else 0
    # eqri
    elif ins == "eqri":
        reg[cmd[3]] = 1 if reg[cmd[1]] == cmd[2] else 0
    # eqrr
    else:
        reg[cmd[3]] = 1 if reg[cmd[1]] == reg[cmd[2]] else 0

    reg[ir] += 1

print (reg[0])
