# Answer: 3138510102

from functools import reduce

file = open ("14.txt")
count = int (file.readline ())
file.close ()

# List of recipes
recipes = [3, 7]

# Index of current recipe for each elf
elf1 = 0
elf2 = 1

# Apply recipe process
while len (recipes) < count + 10:
    recipes.extend (map (int, list (str (recipes[elf1] + recipes[elf2]))))
    elf1 = (elf1 + recipes[elf1] + 1) % len (recipes)
    elf2 = (elf2 + recipes[elf2] + 1) % len (recipes)

# Trim excess recipes
while len (recipes) > count + 10:
    del recipes[-1]

print (reduce (lambda x, y: x + str (y), recipes[-10:], ""))
