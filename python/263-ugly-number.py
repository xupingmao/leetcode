# -*- coding:utf-8 -*-  


"""编写一个程序判断给定的数是否为丑数。

丑数就是只包含质因数 2, 3, 5 的正整数。

说明
- 1 是丑数。
- 输入不会超过 32 位有符号整数的范围: [−231,  231 − 1]。

"""

class Solution:
    def isUgly(self, num):
        if num <= 0:
            return False
        
        while num >= 1:
            if num % 2 == 0:
                num /= 2
            elif num % 3 == 0:
                num /= 3
            elif num % 5 == 0:
                num /= 5
            elif num == 1:
                return True
            else:
                return False

def test(input, expected):
    s = Solution()
    output = s.isUgly(*input)
    if output != expected:
        raise

test([6], True)
test([8], True)
test([14], False)
