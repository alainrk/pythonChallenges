class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def invisit(root):
    l = []
    if root == None:
        return []
    l += invisit(root.left)
    l += [root.value]
    l += invisit(root.right)
    return l

def previsit(root):
    l = []
    if root == None:
        return []
    l += [root.value]
    l += invisit(root.left)
    l += invisit(root.right)
    return l

def isbst(root, mini, maxi):
    if root == None:
        return True
    if root.value <= mini or root.value >= maxi:
        return False
    return isbst(root.left, mini, root.value) and isbst(root.right, root.value, maxi)

def isbst_iter(root):
    if root == None:
        return True
    q = []
    q.append((root,-99999999,99999999))
    while len(q)>0:
        curr = q.pop()
        if curr[0] is None:
            continue
        if curr[0].value < curr[1] or curr[0].value > curr[2]:
            return False
        q.append((curr[0].left, curr[1], curr[0].value))
        q.append((curr[0].right, curr[0].value, curr[2]))
    return True

def gettree(l, start, mini):
    # print "Creating", l[start]," MINI", mini
    curr = l[start]
    n = Node(curr)
    for i in xrange(start+1, len(l)):
        if curr < l[i] and l[i] > mini:
            n.right = gettree(l, i, curr)
            break
        else:
            break
    if start < len(l)-1 and curr > l[start+1]:
        n.left = gettree(l, start+1, curr)
    return n



'''
                    10
                7                 15
            3       9       12             20
        1       8        11    13       17      22
    -5     2
'''

root = Node(10)

root.left = Node(7)
root.left.left = Node(3)
root.left.right = Node(9)
root.left.right.left = Node(8)
root.left.left.left = Node(1)
root.left.left.left.left = Node(-5)
root.left.left.left.right = Node(2)

root.right = Node(15)
root.right.left = Node(12)
root.right.left.left = Node(11)
root.right.left.right = Node(13)
root.right.right = Node(20)
root.right.right.left = Node(17)
root.right.right.right = Node(22)

print isbst_iter(root)

# root = Node(5)
#
# root.left = Node(4)
# root.left.left = Node(2)
# root.left.right = Node(4)
#
# root.right = Node(8)
# root.right.left = Node(6)
# root.right.left.left = Node(9)
#
# print isbst(root, -9999999, 9999999)
# print isbst_iter(root)
#
# p = previsit(root)
# i = invisit(root)
# print p
# print i
#
# tree = gettree(p, 0, len(p))
# print isbst(tree, -9999999, 9999999)
# print isbst_iter(tree)
#
# print invisit(tree)
