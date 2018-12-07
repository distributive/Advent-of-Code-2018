#Answer: 987

import re

file = open ("7.txt")

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

# Set up the time remaining for each step
times = {}
for step in steps.keys ():
    times[step] = ord (step) - 4

# Each iteration is a second of progress
complete = set ()
workers = [None] * 5
time = 0
while len (complete) < len (times):
    # Assign free workers a task
    for i in range (len (workers)):
        if not workers[i]:
            keys = list (steps.keys ())
            keys.sort ()
            for step in keys:
                if set (steps[step]) <= complete:
                    workers[i] = step
                    del steps[step]
                    break
    # Reduce the time left of worked-on tasks
    timeStep = min ([times[step] for step in workers if step])
    for i in range (len (workers)):
        if workers[i]:
            times[workers[i]] -= timeStep
            if times[workers[i]] == 0:
                complete.add (workers[i])
                workers[i] = None
    time += timeStep

print (time)
file.close ()
