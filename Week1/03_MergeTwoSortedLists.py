# https://leetcode.com/problems/merge-two-sorted-lists/
# 21. Merge Two Sorted Lists - i.e. Linked Lists
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tail = dummy = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1, tail = list1.next, tail.next
            else:
                tail.next = list2
                list2, tail = list2.next, tail.next

        if list1 or list2:
            tail.next = list1 if list1 else list2

        return dummy.next


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
        [[1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]],
        [[], [], []],
        [[], [0], [0]]
    ]

    sol = Solution()
    for test in tests:
        list1 = build_list(test[0])
        list2 = build_list(test[1])
        output = sol.mergeTwoLists(list1, list2)
        output = convert_to_list(output)

        if output == test[2]:
            print(output)
        else:
            print(f"Error: Expected { test[2] } but got { output } instead for { test[0] } and { test[1] }")
