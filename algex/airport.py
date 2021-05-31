def airportConnections(airports, routes, startingAirport):
	graph = {airport: [] for airport in airports}
	for route in routes:
		start, end = route
		graph[start].append(end)

	subsets = {airport: set() for airport in airports}
	for airport in airports:
		dfs(graph, airport, subsets[airport])

	uncovered = {airport for airport in airports}
	uncovered -= subsets[startingAirport]
	del subsets[startingAirport]
	addedRoutes = 0

	while len(uncovered) > 0:
		airport = findLargestUncoveredSubset(subsets, uncovered)
		if airport is None:
			break
		for dest in subsets[airport]:
			if dest in subsets and dest != airport:
				del subsets[dest]
		uncovered -= subsets[airport]
		del subsets[airport]
		addedRoutes += 1

	for _ in range(len(subsets)):
		addedRoutes += 1

	return addedRoutes

def findLargestUncoveredSubset(subsets, uncovered):
	maxIntersection, maxAirport = -1, None
	for airport, dests in subsets.items():
		intersection = len(dests.intersection(uncovered))
		if intersection > maxIntersection:
			maxIntersection, maxAirport = intersection, airport
	return maxAirport

def dfs(graph, start, visited):
	visited.add(start)
	for child in graph[start]:
		if child not in visited:
			dfs(graph, child, visited)




input = {
"airports": ["BGI", "CDG", "DEL", "DOH", "DSM", "EWR", "EYW", "HND", "ICN", "JFK", "LGA", "LHR", "ORD", "SAN", "SFO", "SIN", "TLV", "BUD"],
"routes": [
["LGA", "DSM"],
["DSM", "ORD"],
["SIN", "BGI"],
["SIN", "CDG"],
["CDG", "DEL"],
["DEL", "DOH"],
["DEL", "CDG"],
["DEL", "EWR"],
["HND", "ICN"],
["ICN", "JFK"],
["JFK", "LGA"],
["JFK", "SFO"],
["EYW", "LHR"],
["SFO", "ORD"],
["SFO", "LGA"],
["SFO", "SIN"],
["CDG", "EYW"],
["ORD", "HND"],
["HND", "SAN"],
["LGA", "TLV"],
["LGA", "BUD"]
],
"startingAirport": "LGA"
}

airportConnections(input["airports"], input["routes"], input["startingAirport"])