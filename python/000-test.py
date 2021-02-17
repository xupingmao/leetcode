# -*- coding:utf-8 -*-
# @author xupingmao <578749341@qq.com>
# @since 2021/02/17 18:11:56
# @modified 2021/02/17 18:13:06


def test(input, expected):
    import time
    s = Solution()
    t1 = time.time()
    # 需要提前转成字符串，因为执行过程中可能被改变
    input_str = str(input)
    output = s.reverseList(*input)
    t2 = time.time()
    cost = (t2-t1) * 1000
    print("[INFO] input=%s, output=%s, cost=%.2fms" % (input_str, output, cost))

    if str(output) != str(expected):
        raise Exception("[FAIL] input=%s, output=%s, expected=%s" % (input, output, expected))


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        array = []
        node = self
        while node != None:
            array.append(node.val)
            node = node.next
        return str(array)

    def __eq__(self, obj):
        return obj != None and self.val == obj.val


def build_list(*args):
    head = None
    prev = None

    for value in args:
        node = ListNode(value)

        if prev != None:
            prev.next = node

        if head == None:
            head = node

        prev = node

    return head


