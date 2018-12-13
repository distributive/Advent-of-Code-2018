# Answer: 77271
# Relies on the assumption that the net frequency over a single iteration is positive

file = open ("01.txt")

low = 0

freq = 0
freqs = []

for line in file:
    freq += int (line)
    freqs.append (freq)
    if freq < low:
        low = freq

netGain = freq
count = 1
running = True

while running:
    for i in range (len (freqs)):
        if freqs[i] + netGain in freqs:
            print (freqs[i] + netGain)
            running = False
            break
        if freqs[i] < count*netGain + low:
            freqs[i] += netGain
    count += 1

file.close ()
