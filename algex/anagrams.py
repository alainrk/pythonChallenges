# k=max_len(word) | O(nklog(k)) T | O(n*k)
def groupAnagrams(words):
	d = {}
	for word in words:
		sw = "".join(sorted(word))
		if sw not in d:
			d[sw] = []
		d[sw].append(word)
	return [v for v in d.values()]
