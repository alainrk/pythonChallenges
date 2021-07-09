def validStartingCity(distances, fuel, mpg):
	mingas, minc = 0, 0
	gas = 0
	for i in range(1, len(distances)):
		gas += fuel[i - 1] * mpg - distances[i-1]
		if gas < mingas:
			mingas, minc = gas, i
	return minc