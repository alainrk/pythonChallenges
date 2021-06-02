def solution(n):
    roman = ""
    while n>0:
        print n
        if n >= 1000:
            roman+="M"
            n-=1000
        elif n >= 900:
            roman+="CM"
            n-=900
        elif n >= 500:
            roman+="D"
            n-=500
        elif n >= 400:
            roman+="CD"
            n-=400
        elif 100 <= n < 400:
            roman+="C"
            n-=100
        elif n >= 90:
            roman+="XC"
            n-=90
        elif n >= 50:
            roman+="L"
            n-=50
        elif n >= 40:
            roman+="XL"
            n-=40
        elif 10 <= n < 40:
            roman+="X"
            n-=10
        elif n == 9:
            roman+="IX"
            n-=9
        elif n >= 5:
            roman+="V"
            n-=5
        elif n == 4:
            roman+="IV"
            n-=4
        elif 1 <= n < 4:
            roman+="I"
            n-=1
        else:
            print "Error",n
            break
    return roman
