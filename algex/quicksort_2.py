# O(n^2) T | O(log n) S for pivots
def quickSort(array):
	qs(array, 0, len(array) - 1)
	return array

def qs(array, start, end):
	if start >= end:
		return
	pivot = array[start]

	left, right = start + 1, end
	while left <= right:
		if array[left] > pivot and array[right] < pivot:
			array[left], array[right] = array[right], array[left]
		if array[left] <= pivot:
			left += 1
		if array[right] >= pivot:
			right -= 1
	array[right], array[start] = array[start], array[right]

	# optimization space, apply first on shortest
	smallest = "left" if (right - 1 - start) < (end - right + 1) else "right"
	if smallest == "left":
		qs(array, start, right - 1) # left
	qs(array, right + 1, end) # right
	if smallest == "right":
		qs(array, start, right - 1) # left