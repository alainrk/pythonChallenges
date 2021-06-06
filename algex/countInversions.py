def countInversions(array):
	_, count = helper(array)
	return count

def helper(array):
	if len(array) < 2:
		return array, 0

	mid = len(array) // 2
	print('arr=', array)
	print('mid=', mid)
	left, lcount = helper(array[:mid])
	right, rcount = helper(array[mid:])
	l, r, count = 0, 0, 0
	res = []

	print('\tleft=', left)
	print('\tright=', right)
	while l < len(left) and r < len(right):
		if left[l] <= right[r]:
			res.append(left[l])
			l += 1
		else:
			count += mid - l
			res.append(right[r])
			r += 1
	res += left[l:] + right[r:]
	print('res=', res, '\n')
	return res, lcount + count + rcount

countInversions([5, -1, 2, -4, 3, 4, 19, 87, 762, -8, 0])