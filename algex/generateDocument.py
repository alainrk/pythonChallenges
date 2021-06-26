def generateDocument(characters, document):
	chars = {}
	for c in characters:
		if not c in chars:
			chars[c] = 0
		chars[c] += 1
	for c in document:
		if c not in chars:
			return False
		if not chars[c]:
			return False
		chars[c] -= 1
	return True