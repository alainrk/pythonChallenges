def knapsackProblem(items, capacity):
	# [[v0, w0], [v1, w1]]
	dp = [[i for i in range(capacity + 1)] for _ in range(len(items) + 1)]

	for cap in range(len(dp[0])):
		dp[0][cap] = 0

	for i in range(1, len(dp)):
		currVal, currWeight = items[i - 1]
		for cap in range(len(dp[0])):
			if currWeight <= cap:
				dp[i][cap] = max(dp[i-1][cap], dp[i-1][cap - currWeight] + currVal)
			else:
				dp[i][cap] = dp[i-1][cap]

	itemsTaken = construct(dp, items)
	return [dp[-1][-1], itemsTaken]

def construct(dp, items):
	res = []
	i, j = len(dp) - 1, len(dp[0]) -1
	while True:
		if dp[i][j] == 0 or i < 0 or j < 0:
			break
		if dp[i][j] == dp[i - 1][j]:
			i -= 1
		else:
			res.append(i - 1)
			i -= 1
			j -= items[i][1]
	return res

print(knapsackProblem([[1, 2], [4, 3], [5, 6], [6, 7]], 10))

print(knapsackProblem([
    [350, 45],
    [550, 65],
    [100, 50],
    [600, 70],
		], 200))

# print(knapsackProblem([
# [1, 100],
# [350, 45],
# [550, 65],
# [600, 70],
# ], 200) == [1500, [3, 12, 14]])


