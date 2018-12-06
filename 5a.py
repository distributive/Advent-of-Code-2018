#Answer: 11946

file = open ("5.txt")

line = file.readline ()
file.close ()

flag = True
while flag:
    flag = False
    skip = False
    newline = ""
    index = 0
    for i in range (1, len (line)):
        if skip:
            skip = False
        elif line[i].lower () == line[i-1].lower () and line[i] != line[i-1]:
            newline += line[index:i-1]
            index = i+1
            flag = True
            skip = True
    line = newline + line[index:]

print (len (line))
