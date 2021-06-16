def waterfallStreams(array, source):
	above = array[0][:]
	above[source] = -100

	for row in range(1, len(array)):
		curr = array[row][:]
		for i, v in enumerate(above):
			if v >= 0:
				continue
			if curr[i] != 1:
				curr[i] += v
				continue

			acc = v / 2

			r = i
			while r + 1 < len(above):
				r += 1
				if above[r] == 1:
					break
				if curr[r] != 1:
					curr[r] += acc
					break
			l = i
			while l - 1 >= 0:
				l -= 1
				if above[l] == 1:
					break
				if curr[l] != 1:
					curr[l] += acc
					break
		above = curr
	return list(map(lambda x: -x, above))

def printMatrix(array, row, sources):
	for r in range(len(array)):
		if r != row:
			decored = array[r]
		else:
			decored = [array[r][c] if sources[c] == 0 else sources[c] for c in range(len(array[0]))]
		print(f'{r:02}', '|\t', '\t'.join(map(lambda x: '-' if x == 0 else 'x' if x == 1 else str(x), decored)))
	print('-'*20)

print(waterfallStreams([
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	], 8))