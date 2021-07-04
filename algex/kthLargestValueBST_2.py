# This is an input class. Do not edit.
class BST:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right


def findKthLargestValueInBst(tree, k):
	count = [k]
	res = visit(tree, count)
	return res

def visit(tree, count):
	if tree.right:
		res = visit(tree.right, count)
		if res is not None:
			return res
	count[0] -= 1
	if count[0] == 0:
		return tree.value
	if tree.left:
		res = visit(tree.left, count)
		if res is not None:
			return res
	return None