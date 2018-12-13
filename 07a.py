# Answer: BCEFLDMQTXHZGKIASVJYORPUWN

import re

file = open ("07.txt")

# Record steps
steps = {}
for line in file:
    pre  = re.search ("(?<=Step ).", line).group ()
    step = re.search ("(?<=step ).", line).group ()
    if pre not in steps.keys ():
        steps[pre] = []
    if step not in steps.keys ():
        steps[step] = [pre]
    else:
        steps[step].append (pre)

# Find order
complete = set ()
order = ""
while steps.keys ():
    keys = list (steps.keys ())
    keys.sort ()
    for step in keys:
        if set (steps[step]) <= complete:
            nextStep = step
            break
    complete.add (nextStep)
    order += nextStep
    del steps[nextStep]

print (order)
file.close ()
