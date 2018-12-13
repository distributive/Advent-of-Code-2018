# Answer: 1447

import re

file = open ("12.txt")

# Get the initial sequence
padding = 40
sequence = re.search ("[\.|#]+", file.readline ()).group ()
sequence = "."*padding + sequence + "."*padding

# Discard empty line
file.readline ()

# Create ruleset
rules = {}
for line in file:
    rule   = re.search ("[\.|#]+", line).group ()
    result = re.search ("[\.|#]$", line).group ()
    rules[rule] = result

# Apply generations
for i in range (20):
    newSequence = ".."
    for j in range (len (sequence)):
        if j > 1 and j < len (sequence) - 2:
            newSequence += rules[sequence[j-2:j+3]]
    sequence = newSequence + ".."

print (sum ([i-padding for i in range (0, len (sequence)) if sequence[i] == "#"]))
file.close ()
