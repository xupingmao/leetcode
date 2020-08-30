# -*- coding:utf-8 -*-
# @author xupingmao <578749341@qq.com>
# @since 2020/08/30 20:30:43
# @modified 2020/08/30 20:33:03


def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result


for n in range(1, 51):
    print("%03d: %d" % (n, factorial(n)))
