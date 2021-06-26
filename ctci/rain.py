def solve(terrain, seaLevel):
	levels = [0] * len(terrain)
	sinks = []
	for i in range(len(terrain)):
		if seaLevel > terrain[i]:
			levels[i] = seaLevel - terrain[i]
		if terrain[i] < 0:
			sinks.append(i)

	for s in sinks:
		levels[s] = 0

		# left
		localMax = 0
		i = s-1
		while 0 <= i < len(terrain) and terrain[i] < seaLevel and terrain[i] != - 1:
			if terrain[i] > localMax:
				levels[i] = 0
			elif seaLevel > localMax:
				levels[i] = min(levels[i], localMax - terrain[i])
			localMax = max(localMax, terrain[i])
			i -= 1

		# right
		localMax = 0
		i = s+1
		while 0 <= i < len(terrain) and terrain[i] < seaLevel and terrain[i] != - 1:
			if terrain[i] > localMax:
				levels[i] = 0
			elif seaLevel > localMax:
				levels[i] = min(levels[i], localMax - terrain[i])
			localMax = max(localMax, terrain[i])
			i += 1

	lakes = []
	currLake = 0
	for i in range(len(levels)):
		if levels[i] == 0 and currLake > 0:
			lakes.append(currLake)
			currLake = 0
		elif levels[i] > 0:
			currLake += levels[i]

	if currLake > 0:
		lakes.append(currLake)

	print(lakes)
	return lakes

def solveEasy(terrains, seaLevel):
	volumes = []
	water = 0

	for i in range(len(terrains)):
		if seaLevel > terrains[i]:
			water += seaLevel - terrains[i]
		else:
			if water > 0:
				volumes.append(water)
				water = 0
	if water > 0:
		volumes.append(water)
	return volumes


assert(solveEasy([1, 5, 1, 4, 3, 2, 1, 3, 4, 5, 6, 7], 4) == [3, 3, 7])

assert(solve([1, 5, 1, 4, 3, 2, 1, 3, 4, 5, 6, 7], 4) == [3, 3, 7])
assert(solve([1, 5, 1, 4, 3, 2, -1, 3, 4, 5, 6], 5) == [4, 3])
assert(solve([5, 4, 1, 3, 2, -1, 3, 1, 2, 1, 4, 1, 6], 5) == [2, 5, 3])
assert(solve([-1, 2, 1, 3, 1, 3, 1, 2, -1], 4) == [1, 2, 1])
