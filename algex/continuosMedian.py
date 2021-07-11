import bisect

class ContinuousMedianHandler:
	def __init__(self):
		self.median = None
		self.arr = []

	def insert(self, number):
		bisect.insort(self.arr, number)
		mid = len(self.arr) // 2
		self.median = self.arr[mid]
		if len(self.arr) % 2 == 0:
			self.median = (self.arr[mid] + self.arr[mid - 1]) / 2

	def getMedian(self):
			return self.median
