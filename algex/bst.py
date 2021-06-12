class BST:
		def __init__(self, value):
				self.value = value
				self.left = None
				self.right = None

		def insert(self, value):
			if value < self.value:
				if self.left is None:
					self.left = BST(value)
				else:
					self.left.insert(value)
			else:
				if self.right is None:
					self.right = BST(value)
				else:
					self.right.insert(value)
					return self

		def contains(self, value):
			if self.value == value:
				return True
			l = False if not self.left else self.left.contains(value)
			r = False if not self.right else self.right.contains(value)
			return l or r

		def remove(self, value):
			if self is None:
					return self
			if value < self.value:
				self.left = self.left.remove(value)
			elif value > self.value:
					self.right = self.right.remove(value)
			else:
				if self.left is None:
					temp = self.right
					self = None
					return temp
				elif self.right is None:
					temp = self.left
					self = None
					return temp

				temp = self.right.minValueNode()
				self.value = temp.value
				self.right = self.right.remove(temp.value)
			return self

		def minValueNode(self):
			current = self
			while current.left is not None:
				current = current.left
			return current

bst = BST(10)
bst.insert(5)
bst.remove(10)