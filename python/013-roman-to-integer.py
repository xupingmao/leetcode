# encoding=utf-8


class Solution(object):

    
                
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        def match(keys, factor, s):
            for i in range(len(keys)-1, -1, -1):
                v = factor * (i+1)
                key = keys[i]
                if s.find(key) == 0:
                    return v, s[len(key):]
            return 0, s

        value = 0
        prev = ''
        thousand = ['M', 'MM', 'MMM']
        hundred = ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        tenth = ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        single = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        v1, rest = match(thousand, 1000, s)
        v2, rest = match(hundred, 100, rest)
        v3, rest = match(tenth, 10, rest)
        v4, rest = match(single, 1, rest)
        return v1+v2+v3+v4
        
    
    
# I -> 1
# V -> 5
# X -> 10
# L -> 50
# C -> 100
# D -> 500
# M -> 1000

# XLV -> 45
# XCIX -> 99
# VIII -> 8
# XL -> 40
# M CM LXXX IV -> 1984

def test(s, expected):
    assert Solution().romanToInt(s) == expected

if __name__ == '__main__':
    test('I', 1)
    test('IX', 9)
    test('VIII', 8)
    test('XLV', 45)
    test('XCIX', 99)
    test('XL', 40)
    test('MCMLXXXIV', 1984)

