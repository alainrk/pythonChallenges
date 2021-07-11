def validIPAddresses(string):
	ips = solve(string, 4)
	res = set()
	for ip in ips:
		tmp = '.'.join(ip)
		if len(tmp) == len(string) + 3:
			res.add(tmp)
	return [x for x in res]

def solve(string, pieces):
	res = [[]]
	if not string or not pieces:
		return res

	for l in range(1,4):
		chunk = string[0:l]
		if isValidChunk(chunk):
			rest = solve(string[l:], pieces - 1)
			for r in rest:
				res.append([chunk] + r)
	return res

def isValidChunk(string):
	if not string:
		return False
	if string.startswith('0') and len(string) > 1:
		return False
	if int(string) > 255:
		return False
	return True