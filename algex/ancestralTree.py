# This is an input class. Do not edit.
class AncestralTree:
  def __init__(self, name):
    self.name = name
    self.ancestor = None

def getYoungestCommonAncestor(top, d1, d2):
	p1 = list(reversed(pathToTheTop(top, d1)))
	p2 = list(reversed(pathToTheTop(top, d2)))
	i, j = len(p1) - 1, len(p2) - 1
	while i >= 0 and j >= 0:
		if p1[i] == p2[j]:
			return p1[i]
		if i > j:
			i -= 1
		elif i < j:
			j -= 1
		else:
			i -= 1
			j -= 1
	return p2[0]

def pathToTheTop(top, curr):
	path = []
	while curr != top:
		path.append(curr)
		curr = curr.ancestor
	path.append(curr)
	return path