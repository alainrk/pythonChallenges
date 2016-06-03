import sys
import timeit

def gcd(a,b):
	while b:
		a,b = b,a%b
	return a
    
# an(n) = an(n-1) + gcd(n,an(n-1))    
def an(n, g=False, p=0, d=0):
	res, gres, dres, i, cp, cd = [7], [1], [], 1, 0, 0

	while d!=0 or p!=0 or i < n:
		res.append(res[i-1] + gcd(i+1,res[i-1]))
		gn = res[i]-res[i-1]

		if p and gn!=1 and gn not in gres:
			cp+=1
			if cp == p:
				gres.append(gn)
				break

		if d and gn!=1:
			dres.append(res[i]/(i+1))
			cd+=1
			if cd == d:
				return dres

		gres.append(gn)
		i+=1
	return gres if g else c if p else res

def p(n):
    return(list(filter(lambda i:i!=1,an(n,True,n,0))))

def count_ones(n):
    return an(n,True,0,0).count(1)

def max_pn(n):
	return max(p(n))

def anOver(n):
	return an(n, True, 0, n)

if __name__ == "__main__":
	start = timeit.timeit()
	#print an(int(sys.argv[1]),)
	#print an(int(sys.argv[1]), True)
	#print list(set(p(int(sys.argv[1]))))
	#print max_pn(int(sys.argv[1]))
	print anOver(int(sys.argv[1]))
	end = timeit.timeit()
	#print end - start

	
