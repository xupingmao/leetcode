from xutils import *

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def f(head):
            n1 = head.next
            if n1 == None:
                return
            n2 = n1.next
            if n2 == None:
                return
            n3 = n2.next
                
            head.next = n2
            n2.next = n1
            n1.next = n3
            
            f(n1)
            
        h = ListNode('head')
        h.next = head
        f(h)
        return h.next

def t(p, head):
    s = Solution()
    r = s.swapPairs(make_list(head))
    print(r, end='')
    assert make_array(r) == p
    print(' - OK')

t([], [])
t([1,2], [2,1])
t([1,2,3], [2,1,3])
t([1,2,3,4], [2,1,4,3])
t([1,2,3,4,5], [2,1,4,3,5])
    
