import sys
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # 二分法
        maxint = 2147483647
        minint = -2147483648
        def f(a, b):
            if b <= 0:
                return maxint, 0
            if a < b:
                return 0, a
            t = b + b
            # b <= a < b*2
            if a < t:
                return 1, a - b
            else:
                # a < b*2
                v, rest = f(a, t)
                # rest < b
                if b > rest:
                    return v+v, rest
                # b <= rest < b*2
                return v+v+1, rest-b
        minus = False
        if dividend >= 0 and divisor >= 0:
            a = dividend
            b = divisor
        if dividend < 0 and divisor < 0:
            a = -dividend
            b = -divisor
        if dividend >= 0 and divisor < 0:
            a = dividend
            b = -divisor
            minus = True
        if dividend <0 and divisor >= 0:
            a = -dividend
            b = divisor
            minus = True
        v, rest = f(a, b)
        if minus:
            v = -v
        # overflow
        if v > maxint:
            v = maxint
        if v < minint:
            v = minint
        return v
        
        
def t(p, a, b):
    s = Solution()
    v = s.divide(a,b)
    print('%s/%s=%s - %s' % (a,b,v,p))
    assert p == v, 'failed'
t(sys.maxsize,0,0)
t(sys.maxsize,10,0)
t(0, 0, 1)
t(1, 3, 2)
t(4, 4, 1)
t(2, 5, 2)
t(2, 5, 2)
t(1, 5, 3)
t(-1,-5,3)
t(1,-5,-3)
t(2147483647, 2147483647+10,1)
t(-2147483648, 2147483647+10,-1)

