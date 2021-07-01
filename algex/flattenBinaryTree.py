# This is the class of the input root. Do not edit it.
class BinaryTree:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right


def flattenBinaryTree(root):
	l = []
	visit(root, l)
	prev = None
	for node in l:
		node.left = prev
		if prev:
			prev.right = node
		prev = node
	prev.right = None
	return l[0]

def visit(root, l):
	if root.left:
		visit(root.left, l)
	l.append(root)
	if root.right:
		visit(root.right, l)