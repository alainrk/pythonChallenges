# This is an input class. Do not edit.
class AncestralTree:
  def __init__(self, name):
    self.name = name
    self.ancestor = None

def getYoungestCommonAncestor(top, d1, d2):
	dist1 = getDist(top, d1)
	dist2 = getDist(top, d2)
	if dist1 > dist2:
		return getCommonAncestor(abs(dist1 - dist2), d1, d2)
	return getCommonAncestor(abs(dist1 - dist2), d2, d1)


def getCommonAncestor(diff, lower, higher):
	while diff > 0:
		if lower.ancestor:
			lower = lower.ancestor
		diff -= 1
	while lower != higher:
		lower = lower.ancestor
		higher = higher.ancestor
	return lower

def getDist(top, curr):
	dist = 0
	while curr != top:
		dist += 1
		curr = curr.ancestor
	return dist