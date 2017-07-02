# -*- coding:utf-8 -*-  
# Created by xupingmao on 2017/06/18
# 

def overflow(v):
    return v > 2147483647 or v < -2147483648

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if overflow(x):
            return 0
        value = str(x)
        sign = ''
        digits = ''
        for c in value:
            if c in '+-':
                sign += c
            else:
                digits += c
        
        v = list(digits)
        v.reverse()
        result = int(sign + ''.join(v))
        if overflow(result):
            return 0
        return result
        