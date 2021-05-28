def numbersInPi(pi, numbers):
	dictionary = set()
	maxLength = 0
	for num in numbers:
		maxLength = max(maxLength, len(num))
		dictionary.add(num)
	memo = {}
	helper(pi, dictionary, memo)
	return -1 if not pi in memo else memo[pi]

def helper(pi, dictionary, memo):
	if pi in memo:
		return memo[pi]
	if pi in dictionary:
		memo[pi] = 0
		return memo[pi]
	if len(pi) == 1:
		memo[pi] = -1
		return memo[pi]

	minSpaces = float('inf')
	for idx in range(1, len(pi)):
		if pi[:idx] in dictionary:
			res = helper(pi[idx:], dictionary, memo)
			if res > -1:
				minSpaces = min(minSpaces, res)
	memo[pi] = -1 if minSpaces > len(pi) else 1 + minSpaces
	return memo[pi]
