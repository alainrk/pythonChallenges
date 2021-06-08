import heapq
def dijkstrasAlgorithm(start, edges):
	graph = createGraph(edges)

	# cost, node, path-so-far
	q = [(0, start, [])]
	visited = set()
	costs = [-1] * len(edges)

	while len(q) > 0:
		currCost, currNode, currPath = heapq.heappop(q)
		if currNode in visited:
			continue
		currPath += [currNode]
		visited.add(currNode)

		if costs[currNode] == -1:
			costs[currNode] = currCost

		for neigh, dist in graph[currNode].items():
			heapq.heappush(q, (currCost + dist, neigh, currPath))
	return costs

def createGraph(edges):
	graph = {}
	for n, links in enumerate(edges):
		graph[n] = {}
		for neigh, dist in links:
			graph[n][neigh] = dist
	return graph

dijkstrasAlgorithm(0, [
    [
      [1, 7]
    ],
    [
      [2, 6],
      [3, 20],
      [4, 3]
    ],
    [
      [3, 14]
    ],
    [
      [4, 2]
    ],
    [],
    []
  ])