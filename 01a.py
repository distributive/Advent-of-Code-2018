# Answer: 538

file = open ("01.txt")

freq = 0

for line in file:
    freq += int (line)

print (freq)
file.close ()
