import re
def my_parse_int(string):
    result = re.sub(ur'\s', u"", string)
    print result
    return int(result) if result.isdigit() and len(re.findall(ur'\d+\s\d+', string))


print my_parse_int("5")
print my_parse_int("55")
print my_parse_int("asd")
print my_parse_int("5 5")
print my_parse_int("")
print my_parse_int(" ")
print my_parse_int(" 5 6    8")
print my_parse_int("              8")
print my_parse_int("8            ")
print my_parse_int("asd            ")
print my_parse_int("  5g            ")
print my_parse_int("5g")
