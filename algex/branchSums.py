class BinaryTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

def solve(node, partSum = 0, solution = []):
  if node.left is None and node.right is None:
    solution.append(node.value + partSum)
    return
  if node.left is not None:
    solve(node.left, partSum + node.value, solution)
  if node.right is not None:
    solve(node.right, partSum + node.value, solution)

def branchSums(root):
  arr = []
  solve(root, 0, arr)
  return arr