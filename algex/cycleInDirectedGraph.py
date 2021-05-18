def cycleInGraph(edges):
	lenNodes = len(edges)
	visited = [0 for _ in range(lenNodes)]
	stack = [False for _ in range(lenNodes)]
	for i in range(lenNodes):
		res = dfs(edges, visited, stack, i)
		if res:
			return res
	return False

def dfs(edges, visited, stack, node):
	visited[node] = 1
	stack[node] = True
	for c in edges[node]:
		if stack[c]:
			return True
		if visited[c] != 2 and dfs(edges, visited, stack, c):
			return True

	stack[node] = False
	visited[node] = 2
	return False