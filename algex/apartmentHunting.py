def apartmentHunting(blocks, reqs):
	d = [{ r: float('inf') for r in reqs } for _ in range(len(blocks))]
	d[0] = { r: 0 if v else float('inf') for r, v in blocks[0].items() }

	for i in range(1, len(blocks)):
		for r in reqs:
			d[i][r] = 0 if blocks[i][r] else d[i-1][r] + 1

	minblock, minsum = len(blocks) - 1, getBlockSum(d[-1], reqs)
	for i in range(len(blocks) - 2, -1, -1):
		for r in reqs:
			d[i][r] = min(d[i][r], d[i+1][r] + 1)
			currsum = getBlockSum(d[i], reqs)
			if currsum <= minsum and i < minblock:
				minblock, minsum = i, currsum

def getBlockSum(block, reqs):
	s = 0
	for r in reqs:
		s += block[r]
	return s