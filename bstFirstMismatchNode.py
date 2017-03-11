class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self,data):
        if self.data:
            if self.data>data:
                if self.left ==None:
                    self.left=Node(data)
                else: return self.left.insert(data)
            if self.data<=data:
                if self.right == None:
                    self.right=Node(data)
                else: return self.right.insert(data)
        else: self.data=data

y=list()
def preorder(tree):
    if tree:
        global y
        y.append(tree.data)
        #print(tree.data,end=' ')
        preorder(tree.left)
        preorder(tree.right)

x = Node(5)
lst = [4,4,2,8,6,9]
for i in range(len(lst)):
    x.insert(lst[i])

preorder(x)
z = y[:]
y=list()

a = Node(5)
lst1 = [3,2,4,8,7,9]
for j in range(len(lst1)):
    a.insert(lst1[j])

preorder(a)

print y
print z

for i in range(len(y)):
    if y[i] != z[i]:
        print(z[i],',',y[i])
        break
    else: pass
