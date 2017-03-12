class Perm():
    def __init__(self,arr):
        self.hmap = {}
        for i in xrange(len(arr)):
            for j in xrange(i+1,len(arr)):
                self.hmap[(i,j)] = sorted(arr[i:j])


    def req(self,a,b,k):
        # return sorted(self.arr[a:b])[k]
        return k, self.hmap[(a,b)][k], self.hmap[(a,b)]

    def printAll(self):
        for k,v in self.hmap.items():
            print k,v

p = Perm([3,4,5,0,1,2])
print p.req(2,5,2) # return 5
print p.req(1,5,3) # return 5
print p.req(1,5,2) # return 5
print p.req(1,5,1) # return 5
print p.req(3,5,1) # return 5
print p.req(4,5,0) # return 5
