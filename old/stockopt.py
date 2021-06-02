# stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

# get_max_profit(stock_prices_yesterday)
# returns 6 (buying for $5 and selling for $11)

# MAX (s[j] - s[i]) | i<j

def _get_max_profit(s):
    sol = min(s)-min(s)
    for i in xrange(len(s)):
        for j in xrange(i+1, len(s)):
            sol = max(s[j] - s[i], sol)
    return sol

def get_max_profit(s):
    minprice, maxp = s[0], s[1]-s[0]
    for i in s[1:]:
        prof = i - minprice
        maxp = max(maxp, prof)
        minprice = min(minprice, i)
    return maxp



print _get_max_profit([10, 4, 3, 2, 1])
print get_max_profit([10, 4, 3, 2, 1])
