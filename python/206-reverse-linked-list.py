# -*- coding:utf-8 -*-
# @author xupingmao <578749341@qq.com>
# @since 2021/02/17 17:54:30
# @modified 2021/02/17 18:17:51

# Definition for singly-linked list.
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

class Solution:
    def reverseList(self, head):
        current = head
        array = []
        while current != None:
            array.append(current)
            current = current.next

        for i in range(len(array)-1, 0, -1):
            current = array[i]
            prev = array[i-1]
            current.next = prev
        
        if len(array) > 0:
            array[0].next = None
            return array[-1]
        else:
            return None

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

def test(input, expected):
    import time
    s = Solution()
    t1 = time.time()
    input_str = str(input)
    output = s.reverseList(*input)
    t2 = time.time()
    cost = (t2-t1) * 1000
    print("[INFO] input=%s, output=%s, cost=%.2fms" % (input_str, output, cost))
    if str(output) != str(expected):
        raise Exception("[FAIL] input=%s, output=%s, expected=%s" % (input, output, expected))

test([None], None)
test([build_list(1)], build_list(1))
test([build_list(1,2)], build_list(2,1))
test([build_list(1,2,3,4,5)], build_list(5,4,3,2,1))

