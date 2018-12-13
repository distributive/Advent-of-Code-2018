# Answer: 34466

file = open ("08.txt")

line = list (map (int, list (file.readline ().split (" "))))

# Node class
class Node ():
    def __init__ (self):
        self.children = []
        self.metaData = []

    def addChild (self, child):
        self.children.append (child)

    def addMetaData (self, value):
        self.metaData.append (value)

    def getValue (self):
        return (
            sum([self.children[i-1].getValue () for i in self.metaData if i > 0 and i <= len (self.children)])
            if self.children else
            sum (self.metaData)
            )

# Reads the line and creates a tree of nodes
def readNode (index):
    node = Node ()
    newIndex = index + 2
    
    for i in range (line[index], 0, -1):
        data = readNode (newIndex)
        node.addChild (data[0])
        newIndex += data[1]

    metaCount = line[index+1]
    for i in range (metaCount):
        node.addMetaData (line[newIndex])
        newIndex += 1

    return (node, newIndex - index)
    
print (readNode (0)[0].getValue ())
file.close ()
