# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class SuffixTrie:
	def __init__(self, string):
		self.root = {}
		self.endSymbol = "*"
		self.populateSuffixTrieFrom(string)

	def add(self, word):
		curr = self.root
		for char in word:
			if char not in curr:
				curr[char] = {}
			curr = curr[char]
		curr[self.endSymbol] = True

	def populateSuffixTrieFrom(self, string):
		for i in range(len(string) - 1, -1, -1):
			self.add(string[i:])

	def contains(self, string):
		curr = self.root
		for char in string:
			if char not in curr:
				return False
			curr = curr[char]
		return self.endSymbol in curr
