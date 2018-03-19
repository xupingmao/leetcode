from xutils import *

def reverse0(head, k):
    '''head excluded'''
    if k == 1:
        return head, head
    cur = head
    head, last = reverse0(head.next, k-1)
    cur.next = last.next
    last.next = cur
    return head, cur

def reverse(head, k):
    head.next, last = reverse0(head.next, k)
    return head, last

def read_group(head, k):
    '''head excluded'''
    last = head
    for i in range(k):
        if last != None:
            last = last.next
    return head, last

class Solution:
    
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        def f(head, k):
            head, last = read_group(head, k)
            if last != None:
                cur_last = last
                head, last = reverse(head, k)
                f(last, k)
                
        h = ListNode('head')
        h.next = head
        f(h, k)
        return h.next
        

def t(p, head, k):
    s = Solution()
    r = s.reverseKGroup(make_list(head), k)
    print(r, end='')
    assert make_array(r) == p
    print(' - OK')

print(read_group(make_list(['head', 1,2]), 2))
print(read_group(make_list(['head',1,2,3]),2))
print(reverse(make_list(['head',1,2]), 2))
print(reverse(make_list(['head',1,2,3]),3))
    
t([], [], 2)
t([1,2], [2,1], 2)
t([1,2,3], [2,1,3], 2)
t([1,2,3,4], [2,1,4,3], 2)
t([1,2,3,4,5], [2,1,4,3,5], 2)
    
