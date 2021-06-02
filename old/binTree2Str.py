class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def treeToStr(root):
    if root is None:
        return ""
    res = str(root.value)
    left = treeToStr(root.left)
    right = treeToStr(root.right)
    return res + ("("+left+")" if left != "" else "") + ("("+right+")" if right != "" else "")

def strToTree(string):
    tree = []
    par = set(["(",")"])
    number = ""             # Number always is followed by "("
    q = []

    for i, s in enumerate(string):
        try:
            n = int(s)
            number += s
            if string[i+1] in par:
                node = Node(int(number))
        except:
            if s == "-":
                number = "-"

            if s in par and node is not None:
                number = ""
                if len(q) == 0:
                    q.append(node)

                elif q[len(q)-1].left is None:
                    q[len(q)-1].left = node
                    q.append(node)
                    node = None
                elif q[len(q)-1].right is None:
                    q[len(q)-1].right = node
                    q.append(node)
                    node = None

            if s == ")":
                if len(q) > 1:
                    popped = q.pop()
    return q


root = Node(-10)

root.left = Node(7)
root.left.left = Node(3)
root.left.right = Node(9)
root.left.right.left = Node(8)
root.left.left.left = Node(1)
root.left.left.left.left = Node(-5)
root.left.left.left.right = Node(2)

root.right = Node(-15)
root.right.left = Node(12)
root.right.left = Node(12)
root.right.left.left = Node(12)
root.right.left.left.left = Node(12)
root.right.left.left.left.left = Node(12)
root.right.left.left.left.left.left = Node(12)
root.right.left.left.left.left.left.left = Node(12)
root.right.left.left.left.left.left.left.left = Node(12)


stringtree = treeToStr(root)
print stringtree

tree = strToTree(stringtree)
print treeToStr(tree[0])
