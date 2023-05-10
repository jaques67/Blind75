# https://leetcode.com/problems/balanced-binary-tree/
# 110. Balanced Binary Tree
# AlgoMonster: Under DFS on Tree: https://algo.monster/problems/balanced_binary_tree
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:  # 52ms
        return self.tree_height(root) != -1

    # Returns -1 if is not a balanced binary tree. The height if it is.
    def tree_height(self, tree):
        if tree is None:
            return 0

        left_height = self.tree_height(tree.left)
        right_height = self.tree_height(tree.right)
        if left_height == -1 or right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1


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


if __name__ == '__main__':
    tests = [
        [[3, 9, 20, None, None, 15, 7], True],
        [[1, 2, 2, 3, 3, None,None, 4, 4], False],
        [[], True]
    ]

    sol = Solution()
    for test in tests:
        root = build_tree(test[0])
        output = sol.isBalanced(root)

        if output == test[1]:
            print(output)
        else:
            print(f"Error: Expected { test[1] } but got { output } instead for: { test[0] }")
