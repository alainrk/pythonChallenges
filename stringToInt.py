import re
def my_parse_int(string):
    result = re.sub(ur'\s', u"", string)
    return int(result) if result.isdigit() and len(re.findall(ur'\d+\s\d+', string)) == 0 else "NaN"
