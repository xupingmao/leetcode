# -*- coding:utf-8 -*-
# @author xupingmao <578749341@qq.com>
# @since 2020/10/29 00:06:52
# @modified 2020/10/29 00:14:59


class Solution:

    def canConstruct(self, ransomNote, magazine):
        list2 = list(magazine)
        for char in ransomNote:
            if char in list2:
                list2.remove(char)
            else:
                return False
        return True


def test(input, expected):
    s = Solution()
    output = s.canConstruct(*input)
    if output != expected:
        raise Exception("FAIL input=%s, output=%s, expected=%s" % (input, output, expected))


test(["a", "b"], False)
test(["aa", "ab"], False)
test(["aa", "aab"], True)
test(["abc", "aabbcc"], True)
test(["test", "this is a cup of tee"], True)





