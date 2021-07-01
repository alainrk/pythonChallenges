# This is the class of the input root. Do not edit it.
class BinaryTree:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right


def flattenBinaryTree(root):
	lmost, _ = visit(root)
	return lmost

def visit(root):
	if not root.left:
		lmost = root
	else:
		llmost, lrmost = visit(root.left)
		connect(lrmost, root)
		lmost = llmost

	if not root.right:
		rmost = root
	else:
		rlmost, rrmost = visit(root.right)
		connect(root, rlmost)
		rmost = rrmost

	return lmost, rmost

def connect(l, r):
	l.right = r
	r.left = l