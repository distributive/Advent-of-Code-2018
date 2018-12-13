import os
import re

extraWidth = 32
pattern = re.compile ("(?<= Answer: ).*")

print (" ----------------" + "-"*extraWidth)
print ("| Day | Solutions" + " "*extraWidth + "|")
print ("|     | a" + " "*(extraWidth + 6) + "b |")

for i in range (1, 26):
    fileName = ("0" if i < 10 else "") + str(i)
    a = pattern.search (open (fileName + "a.py").readline ()).group () if os.path.exists (fileName + "a.py") else "_"
    b = pattern.search (open (fileName + "b.py").readline ()).group () if os.path.exists (fileName + "a.py") else "_"

    print ("|-----+----------" + "-"*extraWidth + "|")
    print ("| " + fileName + "  | " + a + " "*(extraWidth - len (a) - len(b) + 8) + b + " |")

print (" ----------------" + "-"*extraWidth)
