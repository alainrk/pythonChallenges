'''
triple_double(451999277, 41177722899) == 1 // num1 has straight triple 999s and
                                          // num2 has straight double 99s

triple_double(1222345, 12345) == 0 // num1 has straight triple 2s but num2 has only a single 2

triple_double(12345, 12345) == 0

triple_double(666789, 12345667) == 1
'''

import re
def triple_double(num1, num2):
    return 1 if list(set(re.findall(re.compile(ur'(\d)\1\1'), str(num1))).intersection(re.findall(re.compile(ur'(\d)\1'), str(num2)))) else 0
