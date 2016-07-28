def rgb(r, g, b):
    return "".join(list(map(lambda a: ("0"+str((hex(a if 0<=a<=255 else 0 if a<0 else 255).split('x'))[1]).upper())[-2:],(r,g,b))))
