from queue import Queue

# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def rightSiblingTree(root):
	q = Queue()
	visitedByLevel = {}
	q.put((root, 0))

	while not q.empty():
		curr, currLevel = q.get()
		if currLevel not in visitedByLevel:
			visitedByLevel[currLevel] = []
		visitedByLevel[currLevel].append(curr)
		# Empty children
		if curr == None:
			continue
		q.put((curr.left, currLevel + 1))
		q.put((curr.right, currLevel + 1))
		curr.right = None

	for level, nodes in visitedByLevel.items():
		for i in range(len(nodes) - 1):
			if nodes[i] is None:
				continue
			nodes[i].right = nodes[i + 1]

	return root