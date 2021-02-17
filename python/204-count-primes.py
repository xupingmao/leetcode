# encoding=utf-8

"""统计所有小于非负整数 n 的质数的数量。

示例 1：

输入：n = 10
输出：4
解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。

示例 2：

输入：n = 0
输出：0

示例 3：

输入：n = 1
输出：0
 

提示：

0 <= n <= 5 * 10^6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-primes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

        
def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


class Solution:
    def countPrimes(self, n):
        # 厄拉多塞筛法，简称埃氏筛
        # 如果x是质数, 2x,3x,4x...一定不是质数
        # primes[2]为质数4,6,8,...都不为质数
        # primes[n]在n之前所有的数的倍数都被标记过
        # 如果n不是素数，肯定被标记过，如果没被标记，肯定为素数
        count = 0
        primes = ['1' for i in range(n)]
        for i in range(2, n):
            if primes[i] == '0':
                continue
            if primes[i] == '1':
                step = i
                for j in range(step * 2, n, step):
                    primes[j] = '0'
                count += 1

        return count



def test(input, expected):
    import time
    s = Solution()
    t1 = time.time()
    output = s.countPrimes(*input)
    t2 = time.time()
    cost = (t2-t1) * 1000
    print("[INFO] input=%s, output=%s, cost=%sms" % (input, output, cost))
    if output != expected:
        raise Exception("[FAIL] input=%s, output=%s, expected=%s" % (input, output, expected))


test([10], 4)
test([0], 0)
test([1], 0)
test([5*10**3], 669)
test([5*10**4], 5133)

