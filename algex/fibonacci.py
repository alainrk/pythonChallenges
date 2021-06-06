# O(n) T | O(1) S
def getNthFib(n):
	n -= 1
	fibs = [0, 1]
	while n > 1:
		fibs[0], fibs[1] = fibs[1], fibs[0] + fibs[1]
		n -= 1
	return fibs[n]