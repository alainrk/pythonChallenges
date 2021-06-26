def findThreeLargestNumbers(array):
	m1, m2, m3 = float('-inf'), float('-inf'), float('-inf')
	for i in range(len(array)):
		if array[i] > m3:
			m1, m2, m3 = m2, m3, array[i]
		elif array[i] > m2:
			m1, m2 = m2, array[i]
		elif array[i] > m1:
			m1 = array[i]
	return [m1, m2, m3]