def staircaseTraversal(height, maxSteps, memo={}):
	if height < 1:
		return 1

	key = str(height) + '.' + str(maxSteps)
	if key in memo:
		return memo[key]

	ways = 0
	for i in range(1, min(maxSteps, height) + 1):
		ways += staircaseTraversal(height - i, maxSteps)
	memo[key] = ways
	return ways