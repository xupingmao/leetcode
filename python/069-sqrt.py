import math

class Solution:

    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        last_left = 0

        if x == 1:
            return 1

        while left < right:
            test = (right + left) // 2
            v = test * test
            if v == x:
                return test
            if v < x:
                last_left = test
                left = max(test, left + 1)
            if v > x:
                right = min(test, right - 1)

        return last_left

def test(v):
    s = Solution()

    expect = math.sqrt(v) // 1
    target = s.mySqrt(v)

    if expect != target:
        print("expect %s see %s" % (expect, target))

for i in range(1000):
    test(i)