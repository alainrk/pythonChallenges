class node:
    def __init__(self, value, child):
        self.value = value
        self.end = False
        self.child = {}
        if child is not None:
            self.child[child.value] = child

    def addToken(self, token):
        if len(token) == 0:
            self.end = True
            return
        if token[0] not in self.child:
            self.child[token[0]] = node(token[0], None)
        self.child[token[0]].addToken(token[1:])

    def searchToken(self, token):
        if len(token) == 0:
            return True
        if token[0] in self.child:
            return self.child[token[0]].searchToken(token[1:])
        else:
            return False

    def printMe(self):
        print (self.value, self.child.keys(), self.end)
        for i in self.child.values():
            i.printMe()

    def countLeaves(self):
        return sum(list(map(lambda x: x.countLeaves(), self.child.values()))) + (1 if self.end else 0)

    def getSubtree(self, token):
        if len(token) == 0:
            return self
        if token[0] in self.child:
            return self.child[token[0]].getSubtree(token[1:])
        else:
            return None

    def countOccurrences(self, token):
        subtree = self.getSubtree(token)
        return 0 if (subtree is None) else subtree.countLeaves()

root = node("*", None)
root.addToken("A")
root.addToken("a")
root.addToken("Vaffa")
root.addToken("Vaffrensdfsdfedfsdfsdfssfs")
root.addToken("Vaffrensdfefssfs")
root.addToken("Vaffrensdfsdfsdfssfs")
root.addToken("Vaffrensdfsdfsdxxfs")
root.addToken("Vaffrensxxfssfs")
root.addToken("Vaffrefsdfsdfssfs")
root.addToken("Vaffrefsdfsdfssfsc")
root.addToken("Vaffrefsdfsdfssfsd")
root.addToken("Vaffrefsdfsdfssfse")
root.addToken("Vaffrefsdfsdfssfsr")
root.addToken("Vaffrefsdfsdfssfsgg")
root.addToken("Vaffrefsdfsdfssfscc")
root.addToken("Vaffrefsdfsdfssfsxxx")
root.addToken("Vaffin")
root.addToken("Vaffend")
root.addToken("Bast")
root.addToken("Baste")
root.addToken("Basto")
root.addToken("Baston")
root.addToken("Bastone")
root.addToken("Bastone")
root.addToken("Bastone")
root.addToken("Bastone")
root.addToken("Basqweqweqweqweqwetone")
root.addToken("Basqweqweqweqweqwetone")
root.addToken("Basqweqweqweqweqwetosdfsdfe")
root.addToken("Bastone")
root.addToken("Bastdasdasdasdne")
root.addToken("Bastone")
root.addToken("Bastone")
root.addToken("Bastone")
root.addToken("Bastone")
root.addToken("Bastoner")
root.addToken("Bastonerro")

print root.countOccurrences("A")
print root.countOccurrences("V")
print root.countOccurrences("x")
print root.countOccurrences("X")
print root.countOccurrences("Vx")
print root.countOccurrences("Ax")
print root.countOccurrences("Basx")
print root.countOccurrences("111")
print root.countOccurrences("Bast")
print root.countOccurrences("Bas")
