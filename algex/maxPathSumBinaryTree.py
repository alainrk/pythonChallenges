def maxPathSum(tree):
	_, res = solve(tree)
	return res

def solve(tree):
	if not tree:
		return 0, float('-inf')
	lbranch, lmax = solve(tree.left)
	rbranch, rmax = solve(tree.right)
	maxChildBranch = max(lbranch, rbranch)

	maxSumBranch = max(maxChildBranch + tree.value, tree.value)

	maxSumRoot = max(lbranch + tree.value + rbranch, maxSumBranch)
	maxPathSum = max(lmax, rmax, maxSumRoot)

	return maxSumBranch, maxPathSum
