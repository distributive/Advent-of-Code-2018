# Answer: 538

file = open ("1.txt", "r")

freq = 0

for line in file:
    freq += int (line)

print (freq)
file.close ()

