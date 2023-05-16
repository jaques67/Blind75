# https://leetcode.com/problems/reverse-linked-list/
# 206. Reverse Linked List
# Can be reversed either iteratively or recursively
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList_iterative(self, head: Optional[ListNode]) -> Optional[ListNode]:  # 55ms
        # two pointers
        prev, curr = None, head

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev


    def reverseList_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:  # 63ms
        # if next = null return - null is our base case
        # when back, swap the returned and the current
        if not head:
            return None

        new_head = head
        if head.next:
            new_head = self.reverseList_recursive(head.next)
            head.next.next = head
        head.next = None

        return new_head


def build_list(list):
    tmp = val = ListNode()
    for ll in list:
        tmp.next = ListNode(ll)
        tmp = tmp.next

    return val.next


def convert_to_list(linked_list: ListNode):
    result = []
    while linked_list:
        result.append(linked_list.val)
        linked_list = linked_list.next

    return result


if __name__ == '__main__':
    tests = [
        [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]],
        [[1, 2], [2, 1]],
        [[], []]
    ]

    sol = Solution()
    for test in tests:
        head = build_list(test[0])
        # result = sol.reverseList_iterative(head)
        result = sol.reverseList_recursive(head)
        output = convert_to_list(result)
        if output == test[1]:
            print(output)
        else:
            print(f"Error: Expected { test[1] } but got { output } instead for { test[0] }")
