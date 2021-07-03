def longestPalindromicSubstring(string):
	maxlen, maxi, maxj = 1, 0, 0
	for i in range(len(string)):
		for j in range(i, len(string)):
			s = string[i:j+1]
			if s == s[::-1]:
				if maxlen < len(s):
					maxlen, maxi, maxj = len(s), i, j

	return string[maxi:maxj+1]