def classPhotos(r, b):
	r.sort()
	b.sort()
	if r[0] >= b[0]:
		r, b = b, r
	for i in range(len(r)):
		if r[i] >= b[i]:
			return False
	return True
