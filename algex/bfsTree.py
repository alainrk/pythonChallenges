from queue import Queue

# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
      visit = []
      q = Queue()
      q.put(self)
      while not q.empty():
        curr = q.get()
        visit.append(curr.name)
        for c in curr.children:
          q.put(c)
      return visit