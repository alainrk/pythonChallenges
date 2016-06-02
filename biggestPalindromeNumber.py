from itertools import combinations

def largestPalindrome(num, first=True):
    strnum = str(num)
    nums = {int(i):strnum.count(i) for i in set(strnum)}
    head, tail = [],[]
    while True:
        try:
            two_digit = max(filter(lambda x: nums[x]>1, nums))
            if first:
                if two_digit == 0:
                    raise ValueError('Zero on first iteration')
                else:
                    first = False
            nums[two_digit]-=2
            head += [two_digit]
            tail = [two_digit]+tail
        except:
            try:
                one_digit =  max(filter(lambda x: nums[x]==1, nums))
                head += [one_digit]
                break
            except:
                break
    return int("".join(map(str,head+tail)))

def numeric_palindrome(*args):
    print "args:",args
    m = sorted(map(lambda x: reduce(lambda p,q: p*q, x), [e for s in [list(combinations(args,i)) for i in range(2,len(args)+1)] for e in s]))
    largests = [largestPalindrome(i) for i in m]
    print "products:",m
    print "larg_pals:",largests
    return max(largests)


numeric_palindrome(123,5213,1235)
numeric_palindrome(123,500,1235)
numeric_palindrome(123,5213)
