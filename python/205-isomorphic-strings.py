# -*- coding:utf-8 -*-
# @author xupingmao <578749341@qq.com>
# @since 2021/02/17 17:50:30
# @modified 2021/02/17 17:52:29

class Solution:
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        
        # 每个字符都可以映射到另一个字符（可以使自己本身）
        # 不同字符不能映射到同一个字符
        # 相同字符只能映射到同一个字符
        trans_dict = dict()
        trans_value_set = set()

        for i, c1 in enumerate(s):
            c2 = t[i]
            expect = trans_dict.get(c1)

            if expect is None:
                if c2 in trans_value_set:
                    # 已经使用了，不同构
                    return False
                else:
                    trans_dict[c1] = c2
                    trans_value_set.add(c2)
            else:
                if expect != c2:
                    return False
                else:
                    # 同构的
                    pass
        
        return True


def test(input, expected):
    import time
    s = Solution()
    t1 = time.time()
    output = s.isIsomorphic(*input)
    t2 = time.time()
    cost = (t2-t1) * 1000
    print("[INFO] input=%s, output=%s, cost=%sms" % (input, output, cost))
    if output != expected:
        raise Exception("[FAIL] input=%s, output=%s, expected=%s" % (input, output, expected))


test(["egg", "add"], True)
test(["foo", "bar"], False)
test(["eggdd", "addff"], True)
test(["paper", "title"], True)
