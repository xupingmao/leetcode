# -*- coding:utf-8 -*-  
# Created by xupingmao on 2017/03/21
# 

"""atoi in Python

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. 
Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as 
possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect 
on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists 
because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable 
values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.


"""

class Solution(object):

    def isOverflow(self, numPart):
        return len(numPart) > len("2147483647") or (len(numPart) == len("2147483647") and numPart > "2147483647")

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        index = 0
        length = len(str)
        intValue = 0
        valid = False
        sign = 1
        numPart = ""
        # 处理空白符
        while index < length:
            c = str[index]
            if c in " \t\n\r":
                index += 1
            else:
                break
        # 处理符号
        if index < length:
            if str[index] == "+":
                index += 1
            elif str[index] == '-':
                index += 1
                sign = -1

        # 读取数字部分
        while index < length:
            c = str[index]
            if c in "0123456789":
                numPart+=c
                valid = True
                intValue *= 10
                intValue += ord(c) - ord('0')
                # 这里使用Python作弊了，应该通过字符串来判断
                if self.isOverflow(numPart):
                    if sign == 1:
                        return 2147483647
                    else:
                        return -2147483648
                index += 1
            else:
                break
        if not valid:
            return 0
        return intValue * sign

def testCase(str, expected):
    solution = Solution()
    actual = solution.myAtoi(str)
    assert actual == expected, "expected %s but got %s" % (expected, actual)

def _test():
    """
    >>> _test()
    'OK'
    """
    testCase("1235", 1235)
    testCase("1235565", 1235565)
    testCase("-123", -123)
    testCase("+123", 123)
    testCase(" -123", -123)
    testCase("    ", 0)
    testCase("abc", 0)
    testCase("2147483648", 2147483647)
    testCase("21474836489", 2147483647)
    testCase("-21474836489", -2147483648)
    return "OK"