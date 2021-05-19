'''
i/j  0   a  ab  abc
0    0   1   2   3
y    1   1   2   3
ya   2   1   2   3
yab  3   2   1   2
yabd 4   3   2   RES = 2
'''

'''
i/j  0   a  ab  abc
0    0   1   2   3
y    0   1   2   3
ya   0   1   2   3
yab  0   1   2   3
yabd 0   1   2   3
'''

def levenshteinDistance(str1, str2):
	dists = [[y + x for x in range(len(str2) + 1)] for y in range(len(str1) + 1)]

	for i in range(1, len(str1) + 1):
		for j in range(1, len(str2) + 1):
			if str1[i - 1] == str2[j - 1]:
				dists[i][j] = dists[i - 1][j - 1]
			else:
				dists[i][j] = 1 + min(dists[i - 1][j - 1], dists[i - 1][j], dists[i][j - 1])
	return dists[-1][-1]