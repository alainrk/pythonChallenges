def nextGreaterElement(array):
	result = [-1] * len(array)
	stack = []

	for i in range(2 * len(array) - 1, -1, -1):
		ci = i % len(array)

		while len(stack) > 0:
			if stack[-1] <= array[ci]:
				stack.pop()
			else:
				result[ci] = stack[-1]
				break
		stack.append(array[ci])
	return result

nextGreaterElement([2, -3, 5, 6, 1])