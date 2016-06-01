from itertools import permutations

# https://code.google.com/codejam/contest/32016/dashboard#s=p0


f = open("test","r")
lines = f.read()
c = 0
t = 0
for i in lines.split("\n"):
	if (c % 3 == 2):
		a = map(lambda x:int(x),i.split(" "))
		calc = 0
	elif (c % 3 == 0 and c!=0):
		b = map(lambda x:int(x),i.split(" "))
		calc = 1
	else:
		calc = 0
	if (calc):
		t +=1
		res = 999999999
		for i in permutations(a):
			for j in permutations(b):
				r = reduce(lambda x,y: x+y, map(lambda p: p[0]*p[1], zip(i,j)))
				res = r if (r < res) else res
		print "Case #{}: {}".format(t,res)
	c += 1
f.close()

# Test File
'''
2
3
1 3 -5
-2 4 1
5
1 2 3 4 5
1 0 1 0 1
'''
