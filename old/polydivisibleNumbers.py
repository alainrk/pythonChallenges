'''
A polydivisible number is divisible in an unusual way. The first digit is cleanly divisible by 1, the first two digits are cleanly divisible by 2, the first three by 3 and so on.

The interesting thing about polydivisiblity is that it relates to the underlying number, but not the base it is written in, so if aliens came to Earth and used base 23 (11 fingers on one hand and 12 on the other), no matter what squiggles they used to write numbers, they would find the same numbers polydivisible!

 1232
 1    /1 = 1    Yay!
 12   /2 = 6    Yay!
 123  /3 = 41   Yay!
 1232 /4 = 308  Yay!

  123220
 1      /1 = 1            Yay!
 12     /2 = 6            Yay!
 123    /3 = 41           Yay!
 1232   /4 = 308          Yay!
 12322  /5 = 2464.4       Oh no, that's not a round number!
 123220 /6 = 220536.333r  Oh no, that's not a round number!

  base 6   base 10
 1      = 1       -> 1     /1 = 1     Yay!
 12     = 8       -> 8     /2 = 4     Yay!
 123    = 51      -> 51    /3 = 17    Yay!
 1232   = 308     -> 308   /4 = 77    Yay!
 12322  = 1850    -> 1850  /5 = 370   Yay!
 123220 = 11100   -> 11100 /6 = 1850  Yay!



is_polydivisible("1232", 10)   # => True
is_polydivisible("123220", 10) # => False
is_polydivisible("123220", 6)  # => True
get_polydivisible(22, 10)      # => "32"
get_polydivisible(22, 16)      # => "1A"
get_polydivisible(42, 16)      # => "42"

'''

v = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def base10(n,b):
    return reduce(lambda p,q: p+q, map(lambda x: x[0]*(b**x[1]), zip(map(lambda x: int(x), list(map(lambda i: v.index(i) ,list(n)))), reversed(range(len(n)))))) if b!=10 else int(n)

def tenToBase(n,b):
    r=''
    curr = n
    while curr != 0:
        r = v[curr % b] + r
        curr = curr/b
    return r if n!=0 else "0"

def is_polydivisible(s, b):
    return all([base10(s[:i],b)/i == base10(s[:i],b)/(i*1.0) for i in reversed(range(1,len(str(s))+1))])

def get_polydivisible(n, b):
    i = 0
    c = 0
    while i < n:
        t = tenToBase(c,b)
        i=i+1 if is_polydivisible(t, b) else i
        c=c+1
    return tenToBase(c-1,b)

print get_polydivisible(34, 5)
