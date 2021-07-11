def minimumWaitingTime(queries):
	queries.sort()
	s, p = 0, 0
	for i in range(1, len(queries)):
		s = s + queries[i - 1]
		p += s
	return p