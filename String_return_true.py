
""""
Return True if the substrings John' and 'Mary appear the same number of times in the glven string: otherwise return False.
String comparison should be case insensitive.
"""

def john_marry(str):
    s = str.split('&')
    # print(s)
    s1 = s[0]
    s2 = s[1]
    if s1 in s and s2 in s:
        if s.count(s1) == s.count(s2):
            return True
    return False

print(john_marry('John&Marry'))
