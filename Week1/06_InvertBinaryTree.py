# https://leetcode.com/problems/invert-binary-tree/
# 226. Invert Binary Tree
# Definition for a binary tree node.
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


def build_tree(items: List) -> Optional[TreeNode]:
    n = len(items)
    if n == 0:
        return TreeNode(None)

    def inner(index: int = 0) -> TreeNode:
        if n <= index or items[index] is None:
            return None

        node = TreeNode(items[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)

        return node

    return inner()


def build_list(root: TreeNode) -> List:
    if not root or root.val is None:
        return []

    res = []
    queue = deque([root])  # at least one element in the queue to kick start bfs
    while len(queue) > 0:  # as long as there is element in the queue
        n = len(queue)  # number of nodes in current level, see explanation above
        for _ in range(n):  # dequeue each node in the current level
            node = queue.popleft()
            res.append(node.val)
            for child in [node.left, node.right]:  # enqueue non-null children
                if child is not None:
                    queue.append(child)
    return res


if __name__ == '__main__':
    tests = [
        [[4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]],
        [[2, 1, 3], [2, 3, 1]],
        [[], []]
    ]

    sol = Solution()
    for test in tests:
        val = build_tree(test[0])
        output = sol.invertTree(val)
        output = build_list(output)

        if output == test[1]:
            print(output)
        else:
            print(f"Error: Expected { test[1] } but got { output } instead for: { test[0] }")
