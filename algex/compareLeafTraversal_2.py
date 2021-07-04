# This is an input class. Do not edit.
class BinaryTree:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right


def compareLeafTraversal(tree1, tree2):
	s1, s2 = [tree1], [tree2]
	leaf1, leaf2 = None, None

	while len(s1) or len(s2):
		if leaf1 and leaf2:
			if leaf1.value != leaf2.value:
				return False
			leaf1, leaf2 = None, None

		if not leaf1 and len(s1):
			curr1 = s1.pop()
			if not curr1.left and not curr1.right:
				leaf1 = curr1
			if curr1.left:
				s1.append(curr1.left)
			if curr1.right:
				s1.append(curr1.right)

		if not leaf2 and len(s2):
			curr2 = s2.pop()
			if not curr2.left and not curr2.right:
				leaf2 = curr2
			if curr2.left:
				s2.append(curr2.left)
			if curr2.right:
				s2.append(curr2.right)

	return leaf1.value == leaf2.value