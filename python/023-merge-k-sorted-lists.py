# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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
        head = ListNode('head')
        cur = head
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
            cur.next = ListNode(rv)
            cur = cur.next
        return head.next
    
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        def f(lists):
            if len(lists) == 0:
                return []
            if len(lists) == 1:
                return lists[0]
            if len(lists) == 2:
                return self.mergeTwoLists(lists[0], lists[1])
            mid = len(lists) // 2
            l1 = f(lists[:mid])
            l2 = f(lists[mid:])
            return self.mergeTwoLists(l1, l2)
        
        return f(lists)
        