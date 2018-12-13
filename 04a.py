# Answer: 4716

import re

file = open ("04.txt")

# Sort data
data = []

for line in file:
    data.append (line)
data.sort ()

# Record shift data
shifts = {}
guard = -1
start = 0

for line in data:
    if "#" in line:
        guard = int (re.search ("(?<=#)\d+", line).group ())
        if guard not in shifts:
            shifts[guard] = []
            for i in range (60):
                shifts[guard].append (0)
    else:
        minute = int (re.search ("(?<=:)\d+", line).group ())
        if re.search ("(?<=] ).*", line).group () == "falls asleep":
            start = minute
        else:
            for i in range (start, minute):
                shifts[guard][i] += 1
            
# Find the guard with the most sleep time
maxValue = 0
maxGuard = -1

for guard in shifts.keys ():
    if sum (shifts[guard]) > maxValue:
        maxGuard = guard
        maxValue = sum (shifts[guard])

print (maxGuard * shifts[maxGuard].index (max (shifts[maxGuard])))
file.close ()
