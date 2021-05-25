# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def findSuccessor(tree, node):
	if node.right is not None:
		return findLeftmost(node.right)
	return findLeftyParent(node)

def findLeftyParent(node):
	curr = node
	while curr.parent is not None:
		if curr.parent.left and curr.parent.left.value == curr.value:
			return curr.parent
		curr = curr.parent
	return None

def findLeftmost(node):
	curr = node
	while curr.left:
		curr = curr.left
	return curr