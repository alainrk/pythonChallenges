def topologicalSort(jobs, deps):
	topsort = []
	emptyIns = { j for j in jobs }
	graph = { j: set() for j in jobs }
	back = { j: set() for j in jobs }

	for d in deps:
		graph[d[0]].add(d[1])
		back[d[1]].add(d[0])
		emptyIns.discard(d[1])

	while len(emptyIns) > 0:
		n = emptyIns.pop()
		topsort.append(n)
		for m in graph[n]: # copy to remove safely
			back[m].discard(n)
			if len(back[m]) == 0:
				emptyIns.add(m)
		# remove all edges for this node
		graph[n] = set()

	if hasEdges(graph): # check loops
		return []
	return topsort

def hasEdges(graph):
	for _, child in graph.items():
		if len(child) > 0:
			return True
	return False