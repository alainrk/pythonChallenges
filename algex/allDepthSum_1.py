def allKindsOfNodeDepths(root):
	return solve(root)

def solve(root):
	s = 0
	s += subSolve(root, 0)
	if root.left:
		s += solve(root.left)
	if root.right:
		s += solve(root.right)
	return s

def subSolve(root, depth):
	s = depth
	if root.left:
		s += subSolve(root.left, depth + 1)
	if root.right:
		s += subSolve(root.right, depth + 1)
	print(f"SubSolve {root.value} = {s}")
	return s

# This is the class of the input binary tree.
class BinaryTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
