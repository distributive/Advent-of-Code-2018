# Answer:
# Assumes all strings are equal length

file = open ("2aInput.txt", "r")

lines = []

for line in file:
    lines.append (line)

for i in range (len (lines)):
    for j in range (i+1, len (lines)):
        errors = 0
        for k in range (len (lines[i])):
            if lines[i][k] != lines[j][k]:
                errors += 1
                if errors > 1:
                    break
        if errors == 1:
            s = ""
            for k in range (len (lines[i])):
                if lines[i][k] == lines[j][k]:
                    s += lines[i][k]
            print (s)

file.close ()
