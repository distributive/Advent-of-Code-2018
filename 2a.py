# Answer: 5456

file = open ("2.txt")

twos = 0
threes = 0

for line in file:
    letters = {}
    for char in line:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1
    two = False
    three = False
    for char in letters:
        if not two and letters[char] == 2:
            two = True
            twos += 1
        elif not three and letters[char] == 3:
            three = True
            threes += 1

print (twos * threes)
file.close ()
