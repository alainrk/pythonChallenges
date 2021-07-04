def longestPalindromicSubstring(string):
	maxLen, start, end = 1, 0, 0
	for i in range(1, len(string)):
		count = 0
		# even
		if string[i-1:i+1] == string[i-1:i+1][::-1]:
			s, e = i-1, i
			count = 0
			while s >= 0 and e < len(string) and string[s] == string[e]:
				count += 2
				s, e = s - 1, e + 1
			if count > maxLen:
				maxLen, start, end = count, s + 1, e - 1

		# odd
		if i+1 < len(string) and string[i-1:i+2] == string[i-1:i+2][::-1]:
			s, e = i-1, i+1
			count = 1
			while s >= 0 and e < len(string) and string[s] == string[e]:
				count += 2
				s, e = s - 1, e + 1
			if count > maxLen:
				maxLen, start, end = count, s + 1, e - 1

	return string[start:end+1]
