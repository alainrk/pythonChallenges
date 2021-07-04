def sortStack(stack):
	if not len(stack):
		return stack

	item = stack.pop()
	stack = sortStack(stack)
	insert(stack, item)
	return stack

def insert(stack, val):
	if not len(stack) or stack[-1] <= val:
		stack.append(val)
		return
	curr = stack.pop()
	insert(stack, val)
	stack.append(curr)