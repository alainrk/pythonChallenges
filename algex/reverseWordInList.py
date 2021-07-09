def reverseWordsInString(string):
	currWord = ''
	currSpaces = 0
	res = ''
	for s in string:
		if s == " ":
			if currWord:
				res = currWord + res
				currWord = ''
			currSpaces += 1
		else:
			if currSpaces:
				res = (' ' * currSpaces) + res
				currSpaces = 0
			currWord += s
	if currSpaces:
		res = (' ' * currSpaces) + res
	if currWord:
		res = currWord + res
	return res