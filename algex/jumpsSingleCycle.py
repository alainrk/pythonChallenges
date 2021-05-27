def hasSingleCycle(array):
	curr, jumps = 0, 0
	while jumps < len(array):
		curr = (curr + array[curr]) % len(array)
		jumps += 1
		if curr == 0 and jumps < len(array):
			return False
	return curr == 0
