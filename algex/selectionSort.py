def selectionSort(array):
	for i in range(len(array) - 1):
		mini, minv = i, array[i]
		for j in range(i + 1, len(array)):
			mini, minv = (j, array[j]) if array[j] < minv else (mini, minv)
		array[i], array[mini] = array[mini], array[i]
	return array