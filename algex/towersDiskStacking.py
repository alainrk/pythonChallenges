from functools import cmp_to_key

def diskStacking(disks):
	disks.sort(key=cmp_to_key(compare))
	disks.reverse()
	maxh = [0] * len(disks)
	towers = []
	for i in range(len(disks)):
		maxh[i] = disks[i][2]
		tower = [disks[i]]
		for j in range(i + 1, len(disks)):
			if compare(disks[j], tower[-1]) == -3:
				maxh[i] += disks[j][2]
				tower.append(disks[j])
		towers.append(tower)
	maxIdx = maxh.index(max(maxh))
	return towers[maxIdx]

def compare(a, b):
	res = 0
	for i in range(3):
		if a[i] < b[i]:
			res -= 1
		if a[i] > b[i]:
			res += 1
	return res

diskStacking([ [2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5] ])