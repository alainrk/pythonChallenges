# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def compareLeafTraversal(tree1, tree2):
	return visit(tree1) == visit(tree2)
	
def visit(tree):
	l = []
	stack = [tree]
	while len(stack):
		curr = stack.pop()
		if not curr.left and not curr.right:
			l.append(curr.value)
		if curr.left:
			stack.append(curr.left)
		if curr.right:
			stack.append(curr.right)
	return l