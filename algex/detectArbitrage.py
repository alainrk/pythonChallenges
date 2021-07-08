from math import log10

def detectArbitrage(rates):
	n = len(rates)
	graph = createGraph(rates)
	print(graph)

	dists = [float('inf')] * n
	dists[0] = 0

	# n-1 relaxations => if loop is at least n-1 steps (with n nodes)
	for _ in range(n-1):
		updated = relaxation(graph, dists)
		# if no updates, no negative cycles
		if not updated:
			return False
	# otherwise, check negative cycle exists => it exists if we can relax edges again
	return relaxation(graph, dists)

def relaxation(graph, dists):
	updated = False
	for s, edge in enumerate(graph):
		for n, val in enumerate(edge):
			newDist = dists[s] + val
			if newDist < dists[n]:
				updated = True
				dists[n] = newDist
	return updated

def createGraph(rates):
	return [[-log10(edge) for edge in row] for row in rates]

def convert(amount, change):
	return amount * change