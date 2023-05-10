# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# 235. Lowest Common Ancestor of a Binary Search Tree
# AlgoMonster: Under DFS/BST: https://algo.monster/problems/lowest_common_ancestor_on_bst
from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':  # 76ms
        # If both are less than current root, search left
        # if both are greater than current root, search right
        # if split between left and right of current root, then current root is CA
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
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
        [[6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], [2], [8], [6]],
        [[6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], [2], [4], [2]],
        [[2, 1], [2], [1], [2]]
    ]

    sol = Solution()
    for test in tests:
        tree = build_tree(test[0])
        p_tree = build_tree(test[1])
        q_tree = build_tree(test[2])

        output = sol.lowestCommonAncestor(tree, p_tree, q_tree)

        result = build_tree(test[3])

        if output.val == result.val:
            print(output.val)
        else:
            print(f"Error: Expected { test[3] } but got { output.val } instead for: { test[0] }")
