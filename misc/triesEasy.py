import json

class Trie:
  def __init__(self):
    self.endChar = '*'
    self.root = {}

  def add(self, word):
    curr = self.root
    for char in word:
      if char not in curr:
        curr[char] = {}
      curr = curr[char]
    curr[self.endChar] = word

  def has(self, word):
    curr = self.root
    for char in word:
      if char not in curr:
        return False
      curr = curr[char]
    return True

trie = Trie()
trie.add('ciao')
trie.add('caio')
trie.add('ciaone')
trie.add('bar')
trie.add('barra')
trie.add('bolla')
trie.add('botta')
trie.add('bottarga')
trie.add('bob')
print(json.dumps(trie.root))

assert(trie.has('bar'))
assert(trie.has('barra'))
assert(not trie.has('*'))
assert(not trie.has('bobx'))
assert(not trie.has('asdf'))