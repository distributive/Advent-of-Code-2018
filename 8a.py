#Answer: 40848

file = open ("8.txt")

line = list (map (int, list (file.readline ().split (" "))))

def readNode (index):
    sumMeta = 0
    newIndex = index + 2
    
    for i in range (line[index], 0, -1):
        data = readNode (newIndex)
        sumMeta += data[0]
        newIndex += data[1]

    metaCount = line[index+1]
    for i in range (metaCount):
        sumMeta += line[newIndex]
        newIndex += 1

    return (sumMeta, newIndex - index)
    
print (readNode (0)[0])
file.close ()
