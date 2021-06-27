from queue import Queue

class Node:
	def __init__(self, key):
		self.key = key
		self.prev = None
		self.next = None

	def delete(self):
		if self.prev:
			self.prev.next = self.next
		if self.next:
			self.next.prev = self.prev

# Do not edit the class below except for the insertKeyValuePair,
# getValueFromKey, and getMostRecentKey methods. Feel free
# to add new properties and methods to the class.
class LRUCache:
	def __init__(self, maxSize):
		self.maxSize = maxSize or 1
		self.size = 0
		self.q = None
		self.last = None
		self.cache = {}

	def touch(self, key):
		isNew = True
		if key in self.cache:
			self.cache[key]["node"].delete()
			isNew = False

		node = Node(key)
		if self.q:
			self.q.prev = node
		node.next = self.q
		self.q = node

		if not self.last:
			self.last = node

		if isNew:
			self.size += 1

		if self.size > self.maxSize:
			del self.cache[self.last.key]
			newLast = self.last.prev
			self.last.delete()
			self.last = newLast
			self.size -= 1
		return node

	def insertKeyValuePair(self, key, value):
		node = self.touch(key)
		self.cache[key] = { "value": value, "node": node }

	def getValueFromKey(self, key):
		if key not in self.cache:
			return None
		self.touch(key)
		return self.cache[key]["value"]

	def getMostRecentKey(self):
		if self.q:
			return self.q.key
		return None


l = LRUCache(3)
l.insertKeyValuePair("b", 2)
l.insertKeyValuePair("a", 1)
l.insertKeyValuePair("c", 3)
l.getMostRecentKey() # "c"
l.getValueFromKey("a") # 1
l.getMostRecentKey() # "a"
l.insertKeyValuePair("d", 4) # 11 3 the cache had 3 entries; the least recently used one is evicted
l.getValueFromKey ("b") # None
l.insertKeyValuePair("a", 5) # 11 "a" already exists in the cache SO its value just gets replaced
l.getValueFromKey("a") # 5