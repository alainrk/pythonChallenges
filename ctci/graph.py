class Node:
  def __init__(self, value):
    self.value = value
    self.visited = False
    self.children = []

  def addChildren(self, nodeArr):
    self.children += nodeArr