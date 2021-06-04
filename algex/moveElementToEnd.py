def moveElementToEnd(array, toMove):
	curr, end = 0, len(array) - 1
	while curr < end:
		if array[curr] == toMove:
			if array[end] == toMove:
				end -= 1
			else:
				array[curr], array[end] = array[end], array[curr]
				curr += 1
				end -= 1
		else:
			curr += 1
	return array

# Easier
def moveElementToEnd2(array, toMove):
	curr, end = 0, len(array) - 1
	while curr < end:
		while curr < end and array[end] == toMove:
				end -= 1
		if array[curr] == toMove:
			array[curr], array[end] = array[end], array[curr]
		curr += 1
	return array
