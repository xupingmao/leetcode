# Definition for singly-linked list.
import sys
from typing import Optional

class ListNode:
    def __init__(self, val=0, next: Optional["ListNode"]=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        new_head = ListNode(next = head)

        node = new_head.next
        prev = new_head
        while node != None:
            node_next = node.next
            # remove node
            prev.next = node.next
            print(f"current={node.val} prev={prev.val} list = ", end='')
            print_list(new_head.next)

            # compare node
            compare_node_prev = new_head
            compare_node = new_head.next
            found = False

            while compare_node != node_next:
                print(f"  compare {compare_node.val} and {node.val}")
                if compare_node.val >= node.val:
                    # find a place to insert
                    compare_node_prev.next = node
                    node.next = compare_node
                    found = True
                    break
                compare_node_prev = compare_node
                compare_node = compare_node.next
            
            if found:
                # prev not changed
                # prev = prev
                node = prev.next
            else:
                # stay here
                prev.next = node
                prev = node
                node = node.next
            
            print("  final ", end="")
            print_list(new_head.next)

        return new_head.next

def make_list(array) -> Optional[ListNode]:
    if len(array) == 0:
        return None
    head = ListNode()
    prev = head
    for value in array:
        node = ListNode(val = value)
        prev.next = node
        prev = node
    return head.next

def list_to_array(head: Optional[ListNode]) -> list:
    if head == None:
        return []
    result = []
    node = head
    while node != None:
        result.append(node.val)
        node = node.next
    return result

def print_list(head: Optional[ListNode]):
    node = head
    while node != None:
        print(node.val, end='')
        if node.next != None:
            print(',', end='')
        node = node.next
    print('')

def test_case(input:list, expect:list):
    head = make_list(input)
    print_list(head)
    result = Solution().insertionSortList(head)
    print_list(result)
    result_list = list_to_array(result)
    if result_list == expect:
        print(f"PASS {input}")
    else:
        print(f"FAIL {input}, expect {expect}, actual {result_list}", file=sys.stderr)

    assert result_list == expect

def main():
    test_case([], [])
    test_case([4,2,1,3], [1,2,3,4])
    test_case([5,3,5,4], [3,4,5,5])
    test_case([1,2,3,4,5], [1,2,3,4,5])
    test_case([5,4,3,2,1], [1,2,3,4,5])

if __name__ == "__main__":
    main()
