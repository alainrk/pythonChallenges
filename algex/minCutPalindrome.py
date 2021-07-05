from queue import Queue

def palindromePartitioningMinCuts(string):
	isPal = [[False for _ in range(len(string))] for _ in range(len(string))]
	for i in range(len(string)):
		for j in range(i, len(string)):
			isPal[i][j] = isPalindrome(string[i:j+1])

	# want to fand the minimum path from i=0 to j=len(string)-1
	# string[i][j] isPal ==> go to string[j][k] that isPal until k = len(string) - 1
	dists = [float('inf')] * len(string)

	for i in range(len(string)):
		if isPal[0][i]:
			dists[i] = 0
		else:
			dists[i] = dists[i - 1] + 1
			for j in range(1, i):
				if isPal[j][i] and dists[j - 1] + 1 < dists[i]:
					dists[i] = dists[j - 1] + 1
	return dists[-1]

def getNeighbours(isPal, curr):
	res = []
	for j, v in enumerate(isPal[curr]):
		if v:
			res.append(j)
	return res

def isPalindrome(string):
	return string == string[::-1]


# print(palindromePartitioningMinCuts('abba')) # 0
# print(palindromePartitioningMinCuts('noonabbad')) # 2
print(palindromePartitioningMinCuts('ababbbabbababa')) # 3
