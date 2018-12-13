# Answer: 4240

import string

file = open ("05.txt")

line = file.readline ()
file.close ()

def react (line):
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
    return len (line)

length = len (line)
for letter in string.ascii_lowercase:
    length = min (length, react (line.replace (letter, "").replace (letter.upper (), "")))

print (length)
