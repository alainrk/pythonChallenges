# This is an input class. Do not edit.
class BinaryTree:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def heightBalancedBinaryTree(tree):
	isBalanced, _ = solve(tree)
	return isBalanced

def solve(tree):
	if not tree:
		return True, 0
	isLeftBalanced, lh = solve(tree.left)
	isRightBalanced, rh = solve(tree.right)
	level = max(lh, rh) + 1
	return isLeftBalanced and isRightBalanced and abs(rh-lh) < 2, level
