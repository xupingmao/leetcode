# encoding=utf-8


problem = """
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.

把数字转成罗马数字

罗马数字共有7个，即Ⅰ（1）、Ⅴ（5）、Ⅹ（10）、Ⅼ（50）、Ⅽ（100）、Ⅾ（500）和Ⅿ（1000）
"""

class Solution(object):

    def do_thousand(self, num_str):
        if len(num_str) <= 3:
            return ""
        n = num_str[-4]
        mapping = {
            "0": "",
            "1": "M",
            "2": "MM",
            "3": "MMM"
        }
        return mapping[n]

    def do_hundred(self, num_str):
        if len(num_str) <= 2:
            return ""
        n = num_str[-3]
        mapping = {
            "0": "",
            "1": "C",
            "2": "CC",
            "3": "CCC",
            "4": "CD",
            "5": "D",
            "6": "DC",
            "7": "DCC",
            "8": "DCCC",
            "9": "CM"
        }
        return mapping[n]

    def do_tenth(self, num_str):
        if len(num_str) <= 1:
            return ""
        n = num_str[-2]
        mapping = {
            "0": "",
            "1": "X",
            "2": "XX",
            "3": "XXX",
            "4": "XL",
            "5": "L",
            "6": "LX",
            "7": "LXX",
            "8": "LXXX",
            "9": "XC"
        }
        return mapping[n]

    def do_single(self, num_str):
        if len(num_str) == 0:
            return ""
        n = num_str[-1]
        mapping = {
            "0": "",
            "1": "I",
            "2": "II",
            "3": "III",
            "4": "IV",
            "5": "V",
            "6": "VI",
            "7": "VII",
            "8": "VIII",
            "9": "IX"
        }
        return mapping[n]

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        num_str = str(num)
        return self.do_thousand(num_str) + self.do_hundred(num_str) + self.do_tenth(num_str) + self.do_single(num_str)


def convert(n):
    return Solution().intToRoman(n)

if __name__ == '__main__':
    assert convert(1) == "I"
    assert convert(11) == "XI"
    assert convert(123) == "CXXIII"
    assert convert(1984) == "MCMLXXXIV"
        


