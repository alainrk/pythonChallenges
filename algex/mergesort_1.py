# Expensive solution
import math
def merge(first, second):
	f, s = 0, 0
	res = []
	while True:
		if f == len(first):
			res += second[s:]
			break
		if s == len(second):
			res += first[f:]
			break
		if first[f] <= second[s]:
			res.append(first[f])
			f += 1
		else:
			res.append(second[s])
			s += 1
	return res

def mergeSort(array):
	if len(array) < 2:
		return array
	middle = math.floor(len(array) / 2)
	first = mergeSort(array[:middle])
	second = mergeSort(array[middle:])
	return merge(first, second)