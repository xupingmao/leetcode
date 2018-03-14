# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        class ListNode:
            def __init__(self, x, next):
                self.val = x
                self.next = next
        
        def remove_from_end(node, prev, nth):
            if node == None:
                return 0
            idx = remove_from_end(node.next, node, nth) + 1
            if nth == idx:
                prev.next = node.next
            return idx
        new_head = ListNode('head', head)
        remove_from_end(head, new_head, n)
        return new_head.next

class ListNode:
    
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
def make_list(array):
    head = ListNode('head')
    cur = head
    for item in array:
        cur.next = ListNode(item)
        cur = cur.next
    return head.next

def make_array(head):
    array = []
    cur = head
    while cur:
        array.append(cur.val)
        cur = cur.next
    return array
        
def test(expected, input, n):
    head = make_list(input)
    s = Solution()
    r = s.removeNthFromEnd(head, n)
    print(expected, make_array(r))
    assert make_array(r) == expected

test([1,2,3], [1,2,3,4], 1)
test([1,2,4], [1,2,3,4], 2)
