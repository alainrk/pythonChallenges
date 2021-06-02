def is_matched(expression):
    stack = []
    opened = ["(","[","{"]
    closed = [")","]","}"]
    for c in expression:
        # print "\nCurrent:",c
        if c in opened:
            # print "Is opened"
            if len(stack) == 0 or stack[-1:][0] in opened:
                stack.append(c)
                # print "Appended", stack
            else:
                # print "Not valid", stack, c, stack[-1:][0]
                return False
        else:
            if len(stack) <= 0:
                return False
            # print "Is closed"
            if (c == ")" and stack[-1:][0] == "(") or (c == "]" and stack[-1:][0] == "[") or (c == "}" and stack[-1:][0] == "{"):
                # print "Match with opened", stack, c
                stack.pop()
                # print "After pop", stack
            else:
                return False
    # print "Final", stack
    return len(stack) == 0


print is_matched("{[()]}")
print is_matched("{)]}")
print is_matched("{[()]")
print is_matched("{[()]}")
print is_matched("[()]}")
print is_matched("{[}")
print is_matched("{[(]}")
print is_matched("{[[[[[[[[[[[(((({{[()]}}))))]]]]]]]]]]]}")
