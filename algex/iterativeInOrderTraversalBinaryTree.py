def iterativeInOrderTraversal(tree, callback):
	curr, prev = tree, None

	while curr is not None:
		# came from above or it's the start
		if prev is None or prev == curr.parent:
			if curr.left is None:
				callback(curr)
				nextn = curr.parent if curr.right is None else curr.right
			else:
				nextn = curr.left
		# came from left
		elif prev == curr.left:
			callback(curr)
			nextn = curr.parent if curr.right is None else curr.right
		# came from right
		else:
			nextn = curr.parent
		# apply pointers
		prev, curr = curr, nextn