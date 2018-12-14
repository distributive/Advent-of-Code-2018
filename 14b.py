# Answer: 3138510102

from functools import reduce

file = open ("14.txt")
sequence = list (map (int, list (file.readline ())))
file.close ()

# List of recipes
recipes = [3, 7]

# Index of current recipe for each elf
elf1 = 0
elf2 = 1

# Apply recipe process until the sequence appears
# Makes use of the fact either one or two recipes can be added at each step
while recipes[-len (sequence):] != sequence and recipes[-len (sequence) - 1:-1] != sequence:
    recipes.extend (map (int, list (str (recipes[elf1] + recipes[elf2]))))
    elf1 = (elf1 + recipes[elf1] + 1) % len (recipes)
    elf2 = (elf2 + recipes[elf2] + 1) % len (recipes)

# Trim excess recipes
if recipes[-len (sequence):] != sequence:
    del recipes[-1]

print (len (recipes) - len (sequence))
