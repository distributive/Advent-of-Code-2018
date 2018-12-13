# Answer: megsdlpulxvinkatfoyzxcbvq
# Assumes all strings are equal length

file = open ("02.txt")

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
                if lines[i][k] == lines[j][k] and lines[i][k] != "\n":
                    s += lines[i][k]
            print (s)

file.close ()
