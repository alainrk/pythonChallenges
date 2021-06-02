def solution(roman):
    num = 0
    jump = False
    for i in range(len(roman)):
        if jump:
            jump = False
            continue
        c = roman[i]
        s = roman[i+1] if i+1 < len(roman) else "Z"
        if c == "M":
            num+=1000
        elif c == "D":
            num+=500
        elif c == "C":
            if s == "M":
                num+=900
                jump = True
            elif s == "D":
                num+=400
                jump = True
            else:
                num+=100
        elif c == "L":
            num+=50
        elif c == "X":
            if s == "C":
                num+=90
                jump = True
            elif s == "L":
                num+=40
                jump = True
            else:
                num+=10
        elif c == "V":
            num+=5
        elif c == "I":
            if s == "X":
                num+=9
                jump = True
            elif s == "V":
                num+=4
                jump = True
            else:
                num+=1
    return num
