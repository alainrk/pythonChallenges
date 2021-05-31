def threeNumberSum(array, targetSum):
	results = []
	array.sort()
	for curr in range(len(array) - 2):
		left, right = curr + 1, len(array) - 1
		while left < right:
			currSum = array[curr] + array[left] + array[right]
			if currSum == targetSum:
				results.append([array[curr], array[left], array[right]])
				left += 1
				right -= 1
			elif currSum < targetSum:
				left += 1
			else:
				right -= 1
	return results
