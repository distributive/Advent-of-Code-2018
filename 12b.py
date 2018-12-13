# Answer: 1050000000480
# Assumes the plants devolve into an increasing single-generation pattern

import re

file = open ("12.txt")

# Get the initial sequence
paddingL = 10
paddingR = 1000
sequence = re.search ("[\.|#]+", file.readline ()).group ()
sequence = "."*paddingL + sequence + "."*paddingR

# Discard empty line
file.readline ()

# Create ruleset
rules = {}
for line in file:
    rule   = re.search ("[\.|#]+", line).group ()
    result = re.search ("[\.|#]$", line).group ()
    rules[rule] = result

# Apply generations to a limit (assume the generations devolve to a linear pattern by generation limit)
limit = 500
for i in range (limit + 2):
    newSequence = ".."
    for j in range (len (sequence)):
        if j > 1 and j < len (sequence) - 2:
            newSequence += rules[sequence[j-2:j+3]]
    sequence = newSequence + ".."
    if i == limit:
        sumLimit = sum ([i-paddingL for i in range (0, len (sequence)) if sequence[i] == "#"])
    if i == limit + 1:
        step = sum ([i-paddingL for i in range (0, len (sequence)) if sequence[i] == "#"]) - sumLimit

print (sumLimit + ((50000000000 - limit - 1) * step))
file.close ()
