from queue import Queue

def invertBinaryTree(tree):
	q = Queue()
	q.put(tree)
	while not q.empty():
		curr = q.get()
		if curr is None:
			continue
		curr.left, curr.right = curr.right, curr.left
		q.put(curr.left)
		q.put(curr.right)

# This is the class of the input binary tree.
class BinaryTree:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
