# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x, next = None):
#         self.val = x
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        cur1 = l1
        cur2 = l2
        result = []
        while cur1 != None or cur2 != None:
            if cur1 != None and cur2 == None:
                rv = cur1.val
                cur1 = cur1.next
            if cur1 == None and cur2 != None:
                rv = cur2.val
                cur2 = cur2.next
            if cur1 != None and cur2 != None:
                r1 = cur1.val
                r2 = cur2.val
                if r1 < r2:
                    rv = r1
                    cur1 = cur1.next
                else:
                    rv = r2
                    cur2 = cur2.next
            result.append(rv)
        return result
            