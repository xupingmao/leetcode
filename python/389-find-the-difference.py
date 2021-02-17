# -*- coding:utf-8 -*-
# @author xupingmao <578749341@qq.com>
# @since 2020/11/07 00:53:46
# @modified 2020/11/07 01:00:59


"""给定两个字符串 s 和 t，它们只包含小写字母。

字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

请找出在 t 中被添加的字母。

"""

class Solution:
    def findTheDifference(self, s, t):
        l1 = list(s)
        l2 = list(t)
        for c in l1:
            l2.remove(c)
        return l2[0]


def test(input, expected):
    s = Solution()
    output = s.findTheDifference(*input)
    if output != expected:
        raise Exception("FAIL input=%s, output=%s, expected=%s" % (input, output, expected))

test(["abcd", "abcde"], "e")
test(["", "y"], "y")
test(["a", "aa"], "a")
test(["ae", "aea"], "a")

