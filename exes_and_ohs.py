"""
Check to see if a string has the same amount of 'x's and 'o's. 
The method must return a boolean and be case insensitive. The string can contain any char.
"""

def xo(s):
    return s.lower().count('o') == s.lower().count('x')

print(xo('ooxx'))
print(xo('xooxx'))
print(xo('ooxXm'))
print(xo('zpzpzpp'))
print(xo('zzoo'))