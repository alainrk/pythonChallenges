# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
	v = []
	visit(tree, v)
	return v[-k]

def visit(tree, v):
	if tree.left:
		visit(tree.left, v)
	v.append(tree.value)
	if tree.right:
		visit(tree.right, v)