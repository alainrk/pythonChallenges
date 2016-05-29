'''

int_to_english(1) == 'one'

int_to_english(10) == 'ten'

int_to_english(25161045656) == 'twenty five billion one hundred sixty one million forty five thousand six hundred fifty six'

'''

import textwrap

basic = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety', 100:'hundred'}
tens = {1:'thousand', 2:'million', 3:'billion', 4:'trillion', 5:'quadrillion', 6:'quintillion', 7:'sextillion', 8:'septillion'}

def triplet(w):
    d = int(w)
    if d in basic:
        return basic[d]
    if d>99:
        return basic[int(w[0])] + " " + basic[100] + " " + triplet("0"+w[1:])
    if d>20:
        return basic[int(w[1])*10] + " " + triplet("00"+w[2])
    return ""

def int_to_english(n):
    n = str(n)
    n = textwrap.wrap("0"+n if len(n)%3==2 else ("00"+n if len(n)%3==1 else n),3)
    res = ""
    for i in reversed(range(len(n))):
        res += triplet(n[len(n)-i-1]) + (" " + tens[i] + " " if i!=0 else "")
    return res.strip()
