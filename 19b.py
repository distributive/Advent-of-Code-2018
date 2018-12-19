# Answer: 18200448
# The commented code will print the input program in pseudo code
# From this I deduced the program (when the first register is set to 1) sets the
# first register to the sum of the factors of 10551394
# It does this by looping through values from 1 to 10551394, 10551394 times
# Technically part a is also a solution to this part, if you set reg = [1]+[0]*5

print (sum ([1,2,7,14,167,334,1169,2338,4513,9026,31591,63182,753671,1507342,5275697,10551394]))

##import re
##
##file = open ("19.txt")
##
### Read data
##ir = int (re.search ("\d", file.readline ()).group ())
##
##print ("Register = [a, b, c, d, e, f]")
##print ("Instruction register = " + "abcdef"[ir])
##i = 0
##
##instructions = []
##for line in file:
##    instructions.append (line)
##
##    ins = line.split (" ")[0]
##    cmd = line.split (" ")
##    cmd = [cmd[0], int (cmd[1]), int (cmd[2]), int (cmd[3])]
##    # addr
##    if ins == "addr":
##        s = "abcdef"[cmd[3]] + " = " + "abcdef"[cmd[1]] + " + " + "abcdef"[cmd[2]]
##    # addi
##    elif ins == "addi":
##        s = "abcdef"[cmd[3]] + " = " + "abcdef"[cmd[1]] + " + " + str (cmd[2])
##    # mulr
##    elif ins == "mulr":
##        s = "abcdef"[cmd[3]] + " = " + "abcdef"[cmd[1]] + " * " + "abcdef"[cmd[2]]
##    # muli
##    elif ins == "muli":
##        s = "abcdef"[cmd[3]] + " = " + "abcdef"[cmd[1]] + " * " + str (cmd[2])
##    # banr
##    elif ins == "banr":
##        s = "abcdef"[cmd[3]] + " = " + "abcdef"[cmd[1]] + " & " + "abcdef"[cmd[2]]
##    # bani
##    elif ins == "bani":
##        s = "abcdef"[cmd[3]] + " = " + "abcdef"[cmd[1]] + " & " + str (cmd[2])
##    # borr
##    elif ins == "borr":
##        s = "abcdef"[cmd[3]] + " = " + "abcdef"[cmd[1]] + " | " + "abcdef"[cmd[2]]
##    # bori
##    elif ins == "bori":
##        s = "abcdef"[cmd[3]] + " = " + "abcdef"[cmd[1]] + " | " + str (cmd[2])
##    # setr
##    elif ins == "setr":
##        s = "abcdef"[cmd[3]] + " = " + "abcdef"[cmd[1]]
##    # seti
##    elif ins == "seti":
##        s = "abcdef"[cmd[3]] + " = " + str (cmd[1])
##    # gtir
##    elif ins == "gtir":
##        s = "abcdef"[cmd[3]] + " = " + "1 if " + str (cmd[1]) + " > " + "abcdef"[cmd[2]] + " else 0"
##    # gtri
##    elif ins == "gtri":
##        s = "abcdef"[cmd[3]] + " = " + "1 if " + "abcdef"[cmd[1]] + " > " + str (cmd[2]) + " else 0"
##    # gtrr
##    elif ins == "gtrr":
##        s = "abcdef"[cmd[3]] + " = " + "1 if " + "abcdef"[cmd[1]] + " > " + "abcdef"[cmd[2]] + " else 0"
##    # eqir
##    elif ins == "eqir":
##        s = "abcdef"[cmd[3]] + " = " + "1 if " + str (cmd[1]) + " == " + "abcdef"[cmd[2]] + " else 0"
##    # eqri
##    elif ins == "eqri":
##        s = "abcdef"[cmd[3]] + " = " + "1 if " + "abcdef"[cmd[1]] + " == " + str (cmd[2]) + " else 0"
##    # eqrr
##    else:
##        s = "abcdef"[cmd[3]] + " = " + "1 if " + "abcdef"[cmd[1]] + " == " + "abcdef"[cmd[2]] + " else 0"
##
##    print ((" " if i < 10 else "") + str (i) + ": " + s)
##    i += 1
##
##file.close ()
